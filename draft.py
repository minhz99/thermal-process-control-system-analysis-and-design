import numpy as np

try:
    import os
    os.environ.setdefault("MPLCONFIGDIR", os.path.join(os.getcwd(), ".mplconfig"))
    try:
        import matplotlib
        matplotlib.use("Agg", force=True)
    except Exception:
        pass
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def step_delay(t, delay):
    return np.maximum(t - delay, 0.0)


def first_order_shape(t, T):
    return 1.0 - np.exp(-t / T)


def fopdt_shape(t, T, L):
    t_shift = step_delay(t, L)
    return (1.0 - np.exp(-t_shift / T)) * (t >= L)


def second_order_shape(t, T1, T2):
    if abs(T1 - T2) < 1e-9:
        tau = 0.5 * (T1 + T2)
        return 1.0 - np.exp(-t / tau) * (1.0 + t / tau)
    return 1.0 - (T1 * np.exp(-t / T1) - T2 * np.exp(-t / T2)) / (T1 - T2)


def sopdt_shape(t, T1, T2, L):
    t_shift = step_delay(t, L)
    return second_order_shape(t_shift, T1, T2) * (t >= L)


def pade_delay(L, n):
    """
    [n/n] Padé xấp xỉ e^{-Ls}.
    Trả về (num, den) theo dạng hệ số đa thức GIẢM dần (phù hợp scipy.signal).
    """
    if L <= 0:
        return np.array([1.0]), np.array([1.0])
    n = int(max(1, n))
    # Hệ số theo công thức Padé cho e^{-x}: num = sum c_k (-x)^k, den = sum c_k (x)^k
    # với c_k = (2n-k)! n! / ((2n)! k! (n-k)!)
    from math import factorial

    c = []
    two_n_fact = factorial(2 * n)
    n_fact = factorial(n)
    for k in range(0, n + 1):
        ck = factorial(2 * n - k) * n_fact / (two_n_fact * factorial(k) * factorial(n - k))
        c.append(ck)

    # Đa thức theo biến s: x = L s
    # mảng hệ số tăng dần theo lũy thừa s (s^0...s^n)
    num_asc = np.array([c[k] * ((-L) ** k) for k in range(n + 1)], dtype=float)
    den_asc = np.array([c[k] * ((L) ** k) for k in range(n + 1)], dtype=float)
    # scipy.signal dùng hệ số giảm dần
    return num_asc[::-1], den_asc[::-1]


def _polyder_desc(p):
    """Đạo hàm đa thức với hệ số GIẢM dần."""
    p = np.asarray(p, dtype=complex)
    deg = len(p) - 1
    if deg <= 0:
        return np.array([0.0], dtype=complex)
    return np.array([p[i] * (deg - i) for i in range(len(p) - 1)], dtype=complex)


def _polyval_desc(p, x):
    """Tính đa thức (hệ số GIẢM dần) tại x."""
    return np.polyval(p, x)


def step_response_via_residues(num_desc, den_desc, t):
    """
    Đáp ứng bậc thang của hệ liên tục G(s)=N(s)/D(s) bằng cách:
      Y(s)=G(s)/s = N(s)/(s D(s))
    và tính tổng thặng dư: y(t)=sum_i r_i e^{p_i t}.

    Giả thiết các cực đơn (simple poles). Kết quả lấy phần thực.
    """
    t = np.asarray(t, dtype=float)
    num_desc = np.asarray(num_desc, dtype=complex)
    den_desc = np.asarray(den_desc, dtype=complex)

    # D_step(s) = s*D(s)
    den_step = np.convolve(den_desc, np.array([1.0, 0.0], dtype=complex))
    num_step = num_desc

    poles = np.roots(den_step)
    d_den_step = _polyder_desc(den_step)

    residues = np.empty_like(poles, dtype=complex)
    for i, p in enumerate(poles):
        residues[i] = _polyval_desc(num_step, p) / _polyval_desc(d_den_step, p)

    # y(t) = sum r_i exp(p_i t)
    exp_term = np.exp(np.outer(t, poles))
    y = exp_term @ residues
    return np.real_if_close(y, tol=1e3).astype(float)


def simulate_high_order_step(t, pade_order=8):
    """
    Mô phỏng đáp ứng bậc thang của hàm truyền bậc cao trong `hàm.png`:
        G(s) = 2.4436 / (2.5833e8 s^6 + 1.4637e8 s^5 + 2.9062e7 s^4
                         + 2.4438e6 s^3 + 7.5588e4 s^2 + 562.387 s + 1) * e^{-43 s}
    Trễ được xấp xỉ bằng Padé [n/n].
    """
    K = 2.4436
    den = np.array(
        [2.5833e8, 1.4637e8, 2.9062e7, 2.4438e6, 7.5588e4, 562.387, 1.0],
        dtype=float,
    )
    num = np.array([K], dtype=float)
    L = 43.0

    num_d, den_d = pade_delay(L, pade_order)
    num_all = np.convolve(num, num_d)
    den_all = np.convolve(den, den_d)
    y = step_response_via_residues(num_all, den_all, t)
    return np.asarray(t, dtype=float), y


def fit_sopdt_to_step(t, y, p0=None):
    """
    Fit SOPDT: G_hat(s) = K / ((1 + T1 s)(1 + T2 s)) * e^{-L s}
    bằng cách khớp đáp ứng bậc thang (grid search thuần NumPy).
    """
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)

    if p0 is None:
        # Gợi ý ban đầu từ `hàm.png` (SOPDT tham khảo)
        p0 = dict(K=2.443, T1=147.94, T2=377.17, L=79.876)

    # Heuristic: gain ~ y(t->inf)
    K_guess = float(np.median(y[-max(20, len(y) // 20) :]))
    K_guess = K_guess if abs(K_guess) > 1e-12 else float(p0["K"])

    total_time = float(t[-1] - t[0])
    # L grid: quanh vùng có trễ (thường lớn), nhưng không vượt quá một phần thời gian mô phỏng
    L_max = max(0.6 * total_time, p0["L"] * 2.0)
    L_grid = np.linspace(0.0, L_max, 80)

    # T grids: logspace phủ rộng, sau đó tinh chỉnh quanh p0
    T_min = max(1.0, total_time / 500.0)
    T_max = max(10.0, total_time * 1.5)
    base = np.geomspace(T_min, T_max, 55)

    # Dùng thêm lưới dày quanh p0 để hội tụ nhanh vào nghiệm hợp lý
    local1 = np.geomspace(max(p0["T1"] / 3.0, T_min), min(p0["T1"] * 3.0, T_max), 35)
    local2 = np.geomspace(max(p0["T2"] / 3.0, T_min), min(p0["T2"] * 3.0, T_max), 35)
    T1_grid = np.unique(np.concatenate([base, local1]))
    T2_grid = np.unique(np.concatenate([base, local2]))

    best = None
    y_norm = max(float(np.max(np.abs(y))), 1.0)

    for L in L_grid:
        for T1 in T1_grid:
            for T2 in T2_grid:
                if T2 < T1:
                    continue
                shape_full = sopdt_shape(t, float(T1), float(T2), float(L))
                denom = float(np.dot(shape_full, shape_full))
                if denom < 1e-18:
                    continue
                # K tối ưu theo LS (không offset)
                K = float(np.dot(y, shape_full) / denom)
                y_hat = K * shape_full
                rmse = float(np.sqrt(np.mean((y_hat - y) ** 2)))
                score = rmse / y_norm
                if best is None or score < best["score"]:
                    best = dict(K=K, T1=float(T1), T2=float(T2), L=float(L), rmse=float(rmse), y_hat=y_hat, score=score)

    if best is None:
        # fallback: dùng p0
        y_hat = float(p0["K"]) * sopdt_shape(t, float(p0["T1"]), float(p0["T2"]), float(p0["L"]))
        rmse = float(np.sqrt(np.mean((y_hat - y) ** 2)))
        return dict(K=float(p0["K"]), T1=float(p0["T1"]), T2=float(p0["T2"]), L=float(p0["L"]), rmse=rmse, y_hat=y_hat, score=rmse / y_norm)

    return best


def estimate_initial_values(t, y):
    y0 = float(np.median(y[: max(3, len(y) // 10)]))
    yss = float(np.median(y[-max(5, len(y) // 8) :]))
    K = yss - y0
    if abs(K) < 1e-6:
        K = float(y[-1] - y[0]) if len(y) > 1 else 1.0
    total_time = max(float(t[-1] - t[0]), 1.0)
    dt = np.diff(t)
    dy = np.diff(y)
    valid = np.abs(dt) > 1e-12
    if np.any(valid):
        slope = dy[valid] / dt[valid]
        slope_t = t[1:][valid]
        threshold = 0.05 * np.max(np.abs(slope)) if np.max(np.abs(slope)) > 0 else 0.0
        active = np.where(np.abs(slope) >= threshold)[0]
        L = float(slope_t[active[0]]) if active.size else 0.0
    else:
        L = 0.0
    return y0, K, total_time, L


def solve_linear_gain(shape, y):
    design = np.column_stack([np.ones_like(shape), shape])
    coeffs, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    y_hat = design @ coeffs
    y0, K = coeffs
    return float(y0), float(K), y_hat


def evaluate_result(name, shape, y, dyn_params):
    y0, K, y_hat = solve_linear_gain(shape, y)
    residual = y - y_hat
    mse = float(np.mean(residual**2))
    rmse = float(np.sqrt(mse))
    sse = float(np.sum(residual**2))
    n = len(y)
    k = 2 + len(dyn_params)
    aic = n * np.log(max(sse / n, 1e-12)) + 2 * k
    return {
        "name": name,
        "params": [y0, K, *dyn_params],
        "rmse": rmse,
        "aic": aic,
        "y_hat": y_hat,
    }


def positive_grid(total_time, num=40):
    return np.geomspace(max(total_time / 200, 1e-3), max(total_time * 1.2, 1.0), num)


def delay_grid(total_time, num=25):
    return np.linspace(0.0, max(total_time * 0.4, 1.0), num)


def search_pt1(t, y, total_time):
    best = None
    for T in positive_grid(total_time, num=60):
        shape = first_order_shape(t, T)
        result = evaluate_result("PT1", shape, y, [float(T)])
        if best is None or result["aic"] < best["aic"]:
            best = result
    return best


def search_fopdt(t, y, total_time):
    best = None
    for T in positive_grid(total_time, num=45):
        for L in delay_grid(total_time, num=30):
            shape = fopdt_shape(t, T, L)
            result = evaluate_result("FOPDT", shape, y, [float(T), float(L)])
            if best is None or result["aic"] < best["aic"]:
                best = result
    return best


def search_pt2(t, y, total_time):
    best = None
    grid = positive_grid(total_time, num=24)
    for T1 in grid:
        for T2 in grid:
            if T2 < T1:
                continue
            shape = second_order_shape(t, T1, T2)
            result = evaluate_result("PT2", shape, y, [float(T1), float(T2)])
            if best is None or result["aic"] < best["aic"]:
                best = result
    return best


def search_sopdt(t, y, total_time):
    best = None
    tau_grid = positive_grid(total_time, num=18)
    l_grid = delay_grid(total_time, num=20)
    for T1 in tau_grid:
        for T2 in tau_grid:
            if T2 < T1:
                continue
            for L in l_grid:
                shape = sopdt_shape(t, T1, T2, L)
                result = evaluate_result("SOPDT", shape, y, [float(T1), float(T2), float(L)])
                if best is None or result["aic"] < best["aic"]:
                    best = result
    return best


def format_model_equation(result):
    p = result["params"]
    if result["name"] == "PT1":
        y0, K, T = p
        return f"y(t) = {y0:.4f} + {K:.4f} * (1 - exp(-t/{T:.4f}))"
    if result["name"] == "FOPDT":
        y0, K, T, L = p
        return f"y(t) = {y0:.4f} + {K:.4f} * (1 - exp(-(t-{L:.4f})/{T:.4f})) , t >= {L:.4f}"
    if result["name"] == "PT2":
        y0, K, T1, T2 = p
        return (
            f"y(t) = {y0:.4f} + {K:.4f} * "
            f"(1 - ({T1:.4f}*exp(-t/{T1:.4f}) - {T2:.4f}*exp(-t/{T2:.4f})) / ({T1:.4f}-{T2:.4f}))"
        )
    y0, K, T1, T2, L = p
    return (
        f"y(t) = {y0:.4f} + {K:.4f} * "
        f"(1 - ({T1:.4f}*exp(-(t-{L:.4f})/{T1:.4f}) - {T2:.4f}*exp(-(t-{L:.4f})/{T2:.4f})) "
        f"/ ({T1:.4f}-{T2:.4f})) , t >= {L:.4f}"
    )


def main():
    # Thoi gian mo phong (chinh tuong doi dai de thay ro tre va qua do)
    t = np.linspace(0.0, 2000.0, 4000)

    # 1) Dap ung qua do cua he bac cao (co tre) trong `ham.png`
    t_hi, y_hi = simulate_high_order_step(t, pade_order=8)

    # 2) Nhan dang SOPDT bang cach fit dap ung bac thang
    fit = fit_sopdt_to_step(t_hi, y_hi)

    print("Nhan dang SOPDT tu dap ung cua he bac cao:")
    print(f"  K  = {fit['K']:.6f}")
    print(f"  T1 = {fit['T1']:.6f}")
    print(f"  T2 = {fit['T2']:.6f}")
    print(f"  L  = {fit['L']:.6f}")
    print(f"  RMSE = {fit['rmse']:.6e}")

    if plt is None:
        return

    # Hinh 1: dac tinh qua do (he bac cao)
    plt.figure(figsize=(10, 5.5))
    plt.plot(t_hi, y_hi, "k", linewidth=2.0, label="Hệ bậc cao (Padé cho trễ)")
    plt.xlabel("Thời gian (s)")
    plt.ylabel("Đáp ứng bậc thang y(t)")
    plt.title("Đặc tính quá độ của hệ bậc cao")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("dac-tinh-qua-do.png", dpi=200)

    # Hinh 2: so sanh he bac cao va SOPDT
    plt.figure(figsize=(10, 5.5))
    plt.plot(t_hi, y_hi, "k", linewidth=2.0, label="Hệ bậc cao")
    plt.plot(t_hi, fit["y_hat"], "r--", linewidth=2.0, label="SOPDT nhận dạng")
    plt.xlabel("Thời gian (s)")
    plt.ylabel("Đáp ứng bậc thang y(t)")
    plt.title("Khớp SOPDT theo đáp ứng bậc thang")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("khep-sopdt.png", dpi=200)
    # Không gọi plt.show() để tránh phụ thuộc GUI/headless.


if __name__ == "__main__":
    main()