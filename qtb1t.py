import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

df = pd.read_csv('dac_tinh_van_dap_ung_xung_1p05.csv')
xdata, ydata = df['T'].values, df['H'].values

def func(t, K, T, to):
    y = K * (1 - np.exp(-(t - to) / T))
    y[t < to] = 0
    return y

def objective(params):
    K, T, to = params
    return np.sum((ydata - func(xdata, K, T, to)) ** 2)

result = minimize(objective, [3.0, 2.0, 4.0], bounds=[(0, None), (0.001, None), (0, None)])
K_opt, T_opt, to_opt = result.x

y_pred = func(xdata, K_opt, T_opt, to_opt)
ss_res = np.sum((ydata - y_pred) ** 2)
r_squared = 1 - ss_res / np.sum((ydata - np.mean(ydata)) ** 2)

x_fit = np.linspace(min(xdata), max(xdata), 200)
plt.figure(figsize=(10, 6))
plt.scatter(xdata, ydata, label='Du lieu goc')
plt.plot(x_fit, func(x_fit, K_opt, T_opt, to_opt), 'r', label='Fit (Q1T)')
plt.xlabel('Time')
plt.ylabel('H')
plt.legend()
plt.title(f'Fit Q1T, R^2 = {r_squared:.4f}')
plt.show()
