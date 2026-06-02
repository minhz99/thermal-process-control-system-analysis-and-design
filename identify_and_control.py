import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from scipy.integrate import odeint

# ----------------- Helper functions for transfer function response -----------------
def fopdt_step(t, K, T, L):
    y = np.zeros_like(t)
    idx = t >= L
    y[idx] = K * (1 - np.exp(-(t[idx] - L) / T))
    return y

def sopdt_step(t, K, T1, T2, L):
    y = np.zeros_like(t)
    idx = t >= L
    t_shift = t[idx] - L
    if abs(T1 - T2) < 1e-6:
        y[idx] = K * (1 - np.exp(-t_shift / T1) * (1 + t_shift / T1))
    else:
        y[idx] = K * (1 - (T1 * np.exp(-t_shift / T1) - T2 * np.exp(-t_shift / T2)) / (T1 - T2))
    return y

# ----------------- Identification -----------------
# 1. Valve (FOPDT)
df_valve = pd.read_csv('van-dap-ung-xung-1,6t.csv', header=None, names=['t', 'y'])
t_v = df_valve['t'].values
y_v = df_valve['y'].values
step_v = 1.6
y_v_norm = y_v / step_v

def obj_valve(params):
    K, T, L = params
    if K <= 0 or T <= 0 or L < 0:
        return 1e9
    y_pred = fopdt_step(t_v, K, T, L)
    return np.sum((y_v_norm - y_pred)**2)

res_v = minimize(obj_valve, [1.0, 5.0, 1.0], method='Nelder-Mead')
K_v, T_v, L_v = res_v.x
print(f"Valve (FOPDT): K={K_v:.4f}, T={T_v:.4f}, L={L_v:.4f}")

# 2. Pressure (SOPDT)
df_pres = pd.read_csv('ap-suat-hoi.csv', header=None, names=['t', 'y'])
t_p = df_pres['t'].values
y_p = df_pres['y'].values
step_p = 1.0 # Assume step is 1.0
y_p_norm = y_p / step_p

def obj_pres(params):
    K, T1, T2, L = params
    if K <= 0 or T1 <= 0 or T2 <= 0 or L < 0:
        return 1e9
    y_pred = sopdt_step(t_p, K, T1, T2, L)
    return np.sum((y_p_norm - y_pred)**2)

res_p = minimize(obj_pres, [1.2, 6.0, 6.0, 4.0], method='Nelder-Mead')
K_p, T1_p, T2_p, L_p = res_p.x
print(f"Pressure (SOPDT): K={K_p:.4f}, T1={T1_p:.4f}, T2={T2_p:.4f}, L={L_p:.4f}")

# ----------------- Controller Design -----------------
# Inner Loop (Valve)
# IMC for FOPDT: lambda_v = L_v (or similar)
lambda_v = max(0.5, L_v)
# PI parameters for FOPDT
Kp_v = T_v / (K_v * (lambda_v + L_v))
Ti_v = T_v

# Outer Loop (Pressure)
# Process is SOPDT: K_p, T1_p, T2_p, L_p
# We design robust controller based on damping index mc
# For SOPDT, approximate as FOPDT for controller tuning:
# Equivalent FOPDT: T_eq = T1_p + T2_p, L_eq = L_p
T_eq = T1_p + T2_p
L_eq = L_p

# Choose mc = 0.972 -> theta_c = 1.95 (from standard robust tables)
theta_c = 1.95
theta = theta_c * L_eq
# PID parameters (converting robust PI/PID formulas)
Kp_p = T_eq / (K_p * theta)
Ti_p = T_eq
Td_p = (T1_p * T2_p) / (T1_p + T2_p)

print(f"Inner PI: Kp={Kp_v:.4f}, Ti={Ti_v:.4f}")
print(f"Outer PID: Kp={Kp_p:.4f}, Ti={Ti_p:.4f}, Td={Td_p:.4f}")

# ----------------- Plotting -----------------
os.makedirs('Hinhve', exist_ok=True)

plt.figure(figsize=(8,5))
plt.plot(t_v, y_v_norm, label='Thực nghiệm (chuẩn hóa)')
plt.plot(t_v, fopdt_step(t_v, K_v, T_v, L_v), '--', label='Mô hình FOPDT')
plt.title('Nhận dạng đáp ứng van (Lưu lượng)')
plt.xlabel('Thời gian (s)')
plt.ylabel('Lưu lượng')
plt.legend()
plt.grid()
plt.savefig('Hinhve/nhan_dang_van.png')

plt.figure(figsize=(8,5))
plt.plot(t_p, y_p_norm, label='Thực nghiệm (chuẩn hóa)')
plt.plot(t_p, sopdt_step(t_p, K_p, T1_p, T2_p, L_p), '--', label='Mô hình SOPDT')
plt.title('Nhận dạng đáp ứng áp suất hơi')
plt.xlabel('Thời gian (s)')
plt.ylabel('Áp suất')
plt.legend()
plt.grid()
plt.savefig('Hinhve/nhan_dang_ap_suat.png')

print("Done plotting identification.")
