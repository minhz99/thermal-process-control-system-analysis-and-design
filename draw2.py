import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

# Tham số bộ quá nhiệt (dạng tích 2 khâu Quán tính bậc nhất)
# K = 9
# T (T1 = T2) = 18.315
# to = 11.68
# R^2 = 0.9984

# Tham số van
# K = 1
# T (T1 = T2) = 1.984
# to = 0.88
# R^2 = 0.9999

K = 1
T1 = 1.984 # hằng số thời gian thứ nhất (s)
T2 = 1.984 # hằng số thời gian thứ hai (s)
delay = 0.881 # trễ 10 giây

# Hàm truyền dạng tích 2 khâu Q1T
num = [K]
den = [T1 * T2, T1 + T2, 1]

G_q1q1 = TransferFunction(num, den)

# Thời gian mô phỏng
t = np.linspace(0, 20, 4000)

# Đáp ứng bậc thang
t_out, y = step(G_q1q1, T=t)

# Mô phỏng trễ thời gian
y_delay = np.zeros_like(y)
idx = t_out >= delay
y_delay[idx] = y[:np.sum(idx)]

# Vẽ
plt.figure()
plt.plot(t_out, y_delay, linewidth=2)
plt.xlabel("Thời gian (s)")
plt.ylabel("Nhiệt độ (°C)")
plt.title("Đáp ứng bậc thang – Dạng tích 2 khâu Q1T (Bộ quá nhiệt O2(s))")
plt.grid(True)
plt.show()