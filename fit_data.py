import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# ======================================
# 1. Hàm mô hình bậc 2 + trễ
# ======================================
def second_order_delay(t, y0, A, wn, zeta, L):
    """
    Hàm bậc 2 có trễ (critically/underdamped/overdamped)
    t: thời gian (s)
    y0: giá trị ban đầu
    A: biên độ
    wn: tần số riêng (rad/s)
    zeta: damping ratio
    L: trễ (s)
    """
    y_model = np.zeros_like(t)
    for i in range(len(t)):
        if t[i] < L:
            y_model[i] = y0
        else:
            td = t[i] - L
            wd = wn * np.sqrt(max(0, 1 - zeta**2))  # bảo vệ khi zeta>1
            phi = np.arccos(min(1, max(-1, zeta)))  # bảo đảm acos hợp lệ
            y_model[i] = y0 + A*(1 - 1/np.sqrt(max(1e-6, 1 - zeta**2)) * np.exp(-zeta*wn*td) * np.sin(wd*td + phi))
    return y_model

# ======================================
# 2. Hàm fit tự động bậc 2 + trễ
# ======================================
def fit_second_order_delay(t, y):
    """
    Fit tham số y0, A, wn, zeta, L từ dữ liệu
    """
    y0_guess = y[0]
    A_guess  = y[-1] - y[0]
    wn_guess = 0.1
    zeta_guess = 0.7
    L_guess = t[0]
    
    p0 = [y0_guess, A_guess, wn_guess, zeta_guess, L_guess]
    bounds = ([y[0]-5, 0, 0.001, 0.01, 0], [y[0]+5, np.inf, 5, 1, t[-1]])
    
    popt, _ = curve_fit(second_order_delay, t, y, p0=p0, bounds=bounds)
    return popt  # y0, A, wn, zeta, L

# ======================================
# 3. Hàm vẽ dữ liệu + mô hình
# ======================================
def plot_model(t, y, y0, A, wn, zeta, L, label_model="Mô hình"):
    t_fit = np.linspace(t.min(), t.max(), 500)
    y_fit = second_order_delay(t_fit, y0, A, wn, zeta, L)
    
    plt.figure(figsize=(10,5))
    plt.scatter(t, y, color='blue', s=20, label='Dữ liệu gốc')
    plt.plot(t_fit, y_fit, color='red', linewidth=2, label=label_model)
    plt.xlabel('t (s)')
    plt.ylabel('h(t)')
    # plt.title('QTB2 có trễ')
    plt.grid(False)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ======================================
# 4. Hàm cho phép tự chỉnh tham số
# ======================================
def interactive_plot(t, y):
    print("Nhập tham số mô hình bậc 2 + trễ (để thử nghiệm):")
    y0 = float(input("y0 (giá trị ban đầu) = "))
    A = float(input("A (biên độ) = "))
    wn = float(input("wn (tần số riêng rad/s) = "))
    zeta = float(input("zeta (damping ratio) = "))
    L = float(input("L (trễ s) = "))
    
    plot_model(t, y, y0, A, wn, zeta, L, label_model="Mô hình tùy chỉnh")

# ======================================
# 5. Main: đọc file và chạy
# ======================================
if __name__ == "__main__":
    # Đọc file CSV
    df = pd.read_csv("bqn2.csv")  # cột x, y
    # df = pd.read_csv("dac_tinh_van_dap_ung_xung_1,05(t).csv")  # cột x, y
    t = df['x'].values
    y = df['y'].values
    
    # Fit tự động
    y0_fit, A_fit, wn_fit, zeta_fit, L_fit = fit_second_order_delay(t, y)
    print("=== Tham số fit tự động ===")
    print(f"y0 = {y0_fit:.4f}, A = {A_fit:.4f}, wn = {wn_fit:.4f}, zeta = {zeta_fit:.4f}, L = {L_fit:.4f}")
    
    # Vẽ đường cong fit
    # plot_model(t, y, y0_fit, A_fit, wn_fit, zeta_fit, L_fit, label_model="Fit tự động")
    plot_model(t, y, 520, 8.91, 0.047, 0.83, 10, label_model="Fit")
    # plot_model(t, y, 0, 1, 0.51, 0.99, 1, label_model="Fit")
    
    # Cho phép tự chỉnh tham số và vẽ
    interactive_plot(t, y)