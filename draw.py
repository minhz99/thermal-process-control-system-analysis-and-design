import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step
from scipy.optimize import minimize

# Tham so
K_v, T_v, tau_v = 1.02, 3.484, 1.923
K_bqn, T1, T2, tau_bqn = 2.09, 18.243, 18.237, 12.367
K_p1, T_i1 = 1.5986, 6.4036

# Ham truyen
O2_num, O2_den = [K_v], [T_v, 1]
R2_num, R2_den = [K_p1 * T_i1, K_p1], [T_i1, 0]
R2O2_num, R2O2_den = [K_p1 * K_v * T_i1, K_p1 * K_v], [T_i1 * T_v, T_i1, 0]
W2_num, W2_den = R2O2_num, [T_i1 * T_v, T_i1 * (1 + K_p1 * K_v), K_p1 * K_v]
O1_num, O1_den = [K_bqn], [T1 * T2, T1 + T2, 1]
G_num, G_den = np.convolve(W2_num, O1_num), np.convolve(W2_den, O1_den)
G = TransferFunction(G_num, G_den)

# Mo phong
t = np.linspace(0, 600, 10000)
t_out, y_G = step(G, T=t)
tau_e = tau_bqn
y_G_delay = np.zeros_like(y_G)
delay_samples = int(tau_e / (t[1] - t[0]))
if delay_samples < len(y_G):
    y_G_delay[delay_samples:] = y_G[:len(y_G) - delay_samples]

# Nhan dang Q1T
def func_q1t(t, K, T, tau):
    y = np.zeros_like(t)
    idx = t >= tau
    if np.sum(idx) > 0:
        y[idx] = K * (1 - np.exp(-(t[idx] - tau) / T))
    return y

def objective(params):
    K, T, tau = params
    return np.sum((y_G_delay - func_q1t(t_out, K, T, tau)) ** 2)

result = minimize(objective, [K_bqn, 40.0, tau_e], bounds=[(0, None), (0.001, None), (0, None)], method='L-BFGS-B')
K_e, T_e, tau_e_identified = result.x

y_pred = func_q1t(t_out, K_e, T_e, tau_e_identified)
ss_res = np.sum((y_G_delay - y_pred) ** 2)
r_squared = 1 - ss_res / np.sum((y_G_delay - np.mean(y_G_delay)) ** 2)

# Ve do thi
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t_out, y_G_delay, 'b-', linewidth=2, label='Dap ung buoc G(s)')
t_fit = np.linspace(0, max(t_out), 1000)
plt.plot(t_fit, func_q1t(t_fit, K_e, T_e, tau_e_identified), 'r--', linewidth=2, label=f'Mo hinh Q1T (R^2 = {r_squared:.4f})')
plt.xlabel('Thoi gian (s)')
plt.ylabel('Bien do')
plt.title('Dap ung buoc cua doi tuong tuong duong va mo hinh Q1T')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim([0, 200])

plt.subplot(2, 1, 2)
error = y_G_delay - func_q1t(t_out, K_e, T_e, tau_e_identified)
plt.plot(t_out, error, 'g-', linewidth=1.5, label='Sai so')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.xlabel('Thoi gian (s)')
plt.ylabel('Sai so')
plt.title('Sai so giua dap ung thuc te va mo hinh Q1T')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim([0, 200])
plt.tight_layout()
plt.savefig('Hinhve/chuong2_dap_ung_G_ZN.png', dpi=300, bbox_inches='tight')
plt.show()

# Tinh toan tham so PID vong ngoai (Ziegler-Nichols)
K_p2 = (1.2 * T_e) / (K_e * tau_e_identified)
T_i2 = 2 * tau_e_identified
T_d2 = 0.5 * tau_e_identified
print(f"K_p2 = {K_p2:.4f}, T_i2 = {T_i2:.4f} s, T_d2 = {T_d2:.4f} s")
