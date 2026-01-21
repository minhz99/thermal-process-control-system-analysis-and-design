import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

# Tham so
K_v, T_v, tau_v = 1.02, 3.484, 1.923
K_bqn, T1, T2, tau_bqn = 2.09, 18.243, 18.237, 12.367
K_p1, T_i1 = 0.2614, 3.484

# Ham truyen
O2_num, O2_den = [K_v], [T_v, 1]
R2_num, R2_den = [K_p1 * T_i1, K_p1], [T_i1, 0]
R2O2_num, R2O2_den = [K_p1 * K_v * T_i1, K_p1 * K_v], [T_i1 * T_v, T_i1, 0]
W2_num, W2_den = R2O2_num, [T_i1 * T_v, T_i1 * (1 + K_p1 * K_v), K_p1 * K_v]
O1_num, O1_den = [K_bqn], [T1 * T2, T1 + T2, 1]
V1_num, V1_den = np.convolve(W2_num, O1_num), np.convolve(W2_den, O1_den)
V1 = TransferFunction(V1_num, V1_den)

# Mo phong
t = np.linspace(0, 600, 10000)
t_out, y_V1 = step(V1, T=t)
tau_V1 = tau_v + tau_bqn
y_V1_delay = np.zeros_like(y_V1)
delay_samples = int(tau_V1 / (t[1] - t[0]))
if delay_samples < len(y_V1):
    y_V1_delay[delay_samples:] = y_V1[:len(y_V1) - delay_samples]

# Ve do thi
plt.figure(figsize=(10, 6))
plt.plot(t_out, y_V1_delay, linewidth=2)
plt.xlabel("Thoi gian (s)")
plt.ylabel("Bien do")
plt.title("Dap ung bac thang cua doi tuong tuong duong vong ngoai $V_1(s)$")
plt.grid(True, alpha=0.3)
plt.xlim([0, 200])
plt.tight_layout()
plt.show()

print(f"tau_V1 = {tau_V1:.3f} s, K_V1 = {K_bqn:.3f}")
