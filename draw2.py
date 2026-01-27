import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step
from scipy.optimize import minimize
import math

# Tham so
K_v, T_v, tau_v = 1.02, 3.484, 1.923
K_bqn, T1, T2, tau_bqn = 2.09, 18.243, 18.237, 12.367
theta_c = 1.95
theta_1 = theta_c * tau_v
K_p1 = 1.0 / (K_v * theta_1)
T_i1 = T_v
PADE_ORDER = 4

# Tien ich ham truyen
def series_tf(num1, den1, num2, den2):
    return np.polymul(num1, num2), np.polymul(den1, den2)

def feedback_tf(num, den):
    den_cl = np.polyadd(den, num)
    return num, den_cl

def delay_pade(tau, order=PADE_ORDER):
    n = int(order)
    if n < 0:
        raise ValueError("PADE_ORDER >= 0")
    if tau == 0 or n == 0:
        return np.array([1.0], dtype=float), np.array([1.0], dtype=float)
    num_asc, den_asc = [], []
    for k in range(n + 1):
        ck = math.factorial(2 * n - k) / (
            math.factorial(n) * math.factorial(n - k) * math.factorial(k)
        )
        den_asc.append(ck * (tau**k))
        num_asc.append(((-1) ** k) * ck * (tau**k))
    num = np.array(list(reversed(num_asc)), dtype=float)
    den = np.array(list(reversed(den_asc)), dtype=float)
    return num, den

# Xay dung cac khau
O2_num, O2_den = np.array([K_v], dtype=float), np.array([T_v, 1.0], dtype=float)
delay_v_num, delay_v_den = delay_pade(tau_v)

R2_num = np.array([K_p1 * T_i1, K_p1], dtype=float)
R2_den = np.array([T_i1, 0.0], dtype=float)

L_num, L_den = series_tf(R2_num, R2_den, O2_num, O2_den)
L_num, L_den = series_tf(L_num, L_den, delay_v_num, delay_v_den)
W2_num, W2_den = feedback_tf(L_num, L_den)

O1_num = np.array([K_bqn], dtype=float)
O1_den = np.array([T1 * T2, T1 + T2, 1.0], dtype=float)
delay_bqn_num, delay_bqn_den = delay_pade(tau_bqn)

V_num, V_den = series_tf(W2_num, W2_den, O1_num, O1_den)
V_num, V_den = series_tf(V_num, V_den, delay_bqn_num, delay_bqn_den)
V = TransferFunction(V_num, V_den)

# Mo phong dap ung bac thang
t = np.linspace(0, 600, 10000)
t_out, y_V = step(V, T=t)

# Mo hinh Q2T co tre va ham muc tieu fit
def func_q2t(t_arr, K, T1p, T2p, tau):
    y = K * (
        1
        - (T1p * np.exp(-(t_arr - tau) / T1p) - T2p * np.exp(-(t_arr - tau) / T2p))
        / (T1p - T2p)
    )
    y = np.array(y, dtype=float)
    y[t_arr < tau] = 0.0
    return y

def objective_q2t(params):
    K, T1p, T2p, tau = params
    if K <= 0 or T1p <= 0 or T2p <= 0 or tau < 0:
        return np.inf
    if abs(T1p - T2p) < 1e-6:
        return np.inf
    y_hat = func_q2t(t_out, K, T1p, T2p, tau)
    return np.sum((y_V - y_hat) ** 2)

# Toi uu tham so Q2T
x0 = np.array([K_bqn, T1, T2, tau_bqn], dtype=float)
bounds = [(0, None), (1e-3, None), (1e-3, None), (0, None)]
result = minimize(objective_q2t, x0, bounds=bounds, method="L-BFGS-B")
K_V, T1p, T2p, tau_V = result.x

y_fit = func_q2t(t_out, K_V, T1p, T2p, tau_V)
ss_res = np.sum((y_V - y_fit) ** 2)
ss_tot = np.sum((y_V - np.mean(y_V)) ** 2)
r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan

# Ve so sanh
plt.figure(figsize=(10, 6))
plt.plot(t_out, y_V, "b-", linewidth=2, label="Dap ung V(s) (mo phong)")
plt.plot(t_out, y_fit, "r--", linewidth=2, label=f"Q2T fit (R$^2$={r_squared:.4f})")
plt.xlabel("Thoi gian (s)")
plt.ylabel("Bien do")
plt.title("So sanh dap ung mo phong va mo hinh Q2T cua doi tuong V(s)")
plt.grid(True, alpha=0.3)
plt.xlim([0, 200])
plt.legend()
plt.tight_layout()
plt.show()

print("=== Tham so vong trong (ben vung) ===")
print(f"theta_c = {theta_c:.3f}, theta_1 = {theta_1:.3f} s")
print(f"Kp1 = {K_p1:.4f}, Ti1 = {T_i1:.4f} s")
print("=== Ket qua fit Q2T cho V(s) ===")
print(f"K_V = {K_V:.4f}")
print(f"T1' = {T1p:.4f} s")
print(f"T2' = {T2p:.4f} s")
print(f"tau_V = {tau_V:.4f} s")
print(f"R^2 = {r_squared:.4f}")