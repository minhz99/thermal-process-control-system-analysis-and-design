import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
# 1. Doc du lieu
df = pd.read_csv('dac_tinh_van_dap_ung_xung_1p05.csv')
xdata = df['T'].values
ydata = df['H'].values
# 2. Mo hinh Q1T
def func(t, K, T, to):
    y = K * (1 - np.exp(-(t - to) / T))
    y[t < to] = 0
    return y
# 3. Ham muc tieu
def objective(params):
    K, T, to = params
    y_pred = func(xdata, K, T, to)
    return np.sum((ydata - y_pred) ** 2)
# 4. Gia tri khoi tao & rang buoc
initial_guess = [3.0, 2.0, 4.0]   # [K, T, to]
bounds = [
    (0, None),        # K >= 0
    (0.001, None),    # T > 0
    (0, None)         # to >= 0
]
# 5. Toi uu
result = minimize(objective, initial_guess, bounds=bounds)
K_opt, T_opt, to_opt = result.x
# 6. In ket qua
print(f'K = {K_opt}, T = {T_opt}, to = {to_opt}')
# 7. Tinh R^2
y_pred = func(xdata, K_opt, T_opt, to_opt)
ss_res = np.sum((ydata - y_pred) ** 2)
ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
r_squared = 1 - ss_res / ss_tot
print(f'R^2 = {r_squared}')
# 8. Ve do thi
x_fit = np.linspace(min(xdata), max(xdata), 200)
y_fit = func(x_fit, K_opt, T_opt, to_opt)
plt.figure(figsize=(10, 6))
plt.scatter(xdata, ydata, label='Du lieu goc')
plt.plot(x_fit, y_fit, 'r', label='Fit (Q1T)')
plt.xlabel('Time')
plt.ylabel('H')
plt.legend()
plt.title(f'Fit Q1T, R^2 = {r_squared:.4f}')
plt.show()