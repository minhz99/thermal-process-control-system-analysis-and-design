import numpy as np
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.signal as sig

def mult(p1, p2):
    return np.convolve(p1, p2)

def add(p1, p2):
    return np.polyadd(p1, p2)

# ---- Inner Loop (Valve) ----
K2 = 1.4137 / 1.6 # Since input step size is 1.6t
T2 = 4.8694
L2 = 0.8213

num_v0 = [K2]
den_v0 = [T2, 1.0]

# Pade 1st order for delay L2
num_p2 = [-L2 / 2.0, 1.0]
den_p2 = [L2 / 2.0, 1.0]

num_v = mult(num_v0, num_p2)
den_v = mult(den_v0, den_p2)

# PI Controller R2
Kp2 = 4.978 # Calculated as T2 / (theta2 * K2) where K2 = 1.4137 / 1.6
Ti2 = 4.8694
num_r2 = [Kp2 * Ti2, Kp2]
den_r2 = [Ti2, 0.0]

# Inner Closed Loop
num_o2 = mult(num_r2, num_v)
den_o2 = mult(den_r2, den_v)
num_c2 = num_o2
den_c2 = add(den_o2, num_o2)

# ---- Outer Loop (Boiler) ----
K1 = 1.2147
T1 = 6.0356
L1 = 4.0457

num_b0 = [K1]
den_b0 = mult([T1, 1.0], [T1, 1.0])

# Pade 1st order for delay L1
num_p1 = [-L1 / 2.0, 1.0]
den_p1 = [L1 / 2.0, 1.0]

num_b = mult(num_b0, num_p1)
den_b = mult(den_b0, den_p1)

# Effective process
num_be = mult(num_c2, num_b)
den_be = mult(den_c2, den_b)

# PID Controller R1
Kp1 = 1.8222
Ti1 = 12.0712
Td1 = 3.0178
num_r1 = [Kp1 * Td1 * Ti1, Kp1 * Ti1, Kp1]
den_r1 = [Ti1, 0.0]

# Outer Closed Loop
num_o1 = mult(num_r1, num_be)
den_o1 = mult(den_r1, den_be)
num_c1 = num_o1
den_c1 = add(den_o1, num_o1)

# ---- Simulation ----
t_sim2 = np.linspace(0.0, 30.0, 600)
sys_closed2 = sig.TransferFunction(num_c2, den_c2)
t2, y2 = sig.step(sys_closed2, T=t_sim2)

t_sim1 = np.linspace(0.0, 80.0, 800)
sys_closed1 = sig.TransferFunction(num_c1, den_c1)
t1, y1 = sig.step(sys_closed1, T=t_sim1)

# ---- Plotting ----
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Subplot 1: Inner Loop
ax1.plot(t2, y2, color="#1f77b4", linewidth=2.5, label="Đáp ứng lưu lượng dầu $y_2(t)$")
ax1.axhline(1.0, color="#2ca02c", linestyle="--", linewidth=1.5, label="Tín hiệu đặt $r_2(t) = 1$")
ax1.set_title("Đáp ứng quá độ của vòng điều khiển lưu lượng dầu (Vòng trong)", fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel("Thời gian (s)", fontsize=11)
ax1.set_ylabel("Lưu lượng chuẩn hóa", fontsize=11)
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(fontsize=10, loc="lower right")
ax1.set_xlim(0, 30)
ax1.set_ylim(0, 1.2)

# Subplot 2: Outer Loop
ax2.plot(t1, y1, color="#d62728", linewidth=2.5, label="Đáp ứng áp suất hơi $y_1(t)$")
ax2.axhline(1.0, color="#2ca02c", linestyle="--", linewidth=1.5, label="Tín hiệu đặt $z(t) = 1$")
ax2.set_title("Đáp ứng quá độ của vòng điều khiển áp suất hơi (Cascade toàn mạch)", fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel("Thời gian (s)", fontsize=11)
ax2.set_ylabel("Áp suất hơi chuẩn hóa", fontsize=11)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(fontsize=10, loc="lower right")
ax2.set_xlim(0, 80)
ax2.set_ylim(0, 1.2)

plt.tight_layout()
os.makedirs("/Users/minhz/Desktop/HUST/KS/Phân tích và tổng hợp hệ thống điều khiển quá trình nhiệt/btl-dk/Hinhve", exist_ok=True)
plt.savefig("/Users/minhz/Desktop/HUST/KS/Phân tích và tổng hợp hệ thống điều khiển quá trình nhiệt/btl-dk/Hinhve/step_response.png", dpi=300)
print("Simulation plot generated successfully at Hinhve/step_response.png")
