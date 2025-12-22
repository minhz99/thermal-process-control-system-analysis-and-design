import numpy as np
import matplotlib.pyplot as plt

# Tham số fit (ví dụ của bạn)
y0 = 520
A = 8.91
wn = 0.047
zeta = 0.83
L = 10

y0 = 0
A = 1
wn = 0.51
zeta = 0.99
L = 1

# Hàm bậc 2 + trễ
def second_order_delay(t, y0, A, wn, zeta, L):
    y_model = np.zeros_like(t)
    for i in range(len(t)):
        if t[i] < L:
            y_model[i] = y0
        else:
            td = t[i] - L
            wd = wn * np.sqrt(max(0, 1 - zeta**2))
            phi = np.arccos(min(1, max(-1, zeta)))
            y_model[i] = y0 + A*(1 - 1/np.sqrt(max(1e-6, 1 - zeta**2)) * np.exp(-zeta*wn*td) * np.sin(wd*td + phi))
    return y_model

# Tạo thời gian vẽ
t = np.linspace(0, 20, 500)
y = second_order_delay(t, y0, A, wn, zeta, L)

# Vẽ đồ thị chỉ đường fit
plt.figure(figsize=(10,5))
plt.plot(t, y, color='red', linewidth=2, label='Đường fit bậc 2 + trễ')
plt.axvline(L, color='green', linestyle='--', label=f'Trễ L = {L:.2f}s')
plt.xlabel('Thời gian t (s)')
plt.ylabel('Đầu ra y(t)')
plt.title('Đường cong quá trình bậc 2 + trễ (chỉ đường fit)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()