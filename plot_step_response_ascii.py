import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.signal as sig


def mult(p1, p2):
    return np.convolve(p1, p2)


def add(p1, p2):
    return np.polyadd(p1, p2)


# FOPDT: G(s)=K/(T*s+1)*e^(-L*s) with Pade order 1 for delay
def fopdt(K, T, L):
    num0 = [K]
    den0 = [T, 1.0]
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)


# SOPDT: G(s)=K/((T1*s+1)(T2*s+1))*e^(-L*s)
def sopdt(K, T1, T2, L):
    num0 = [K]
    den0 = mult([T1, 1.0], [T2, 1.0])
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)


# PI controller: R(s)=Kp*(1+1/(Ti*s))
def pi_controller(Kp, Ti):
    num = [Kp * Ti, Kp]
    den = [Ti, 0.0]
    return num, den


# PID controller: R(s)=Kp*(1+1/(Ti*s)+Td*s)
def pid_controller(Kp, Ti, Td):
    num = [Kp * Td * Ti, Kp * Ti, Kp]
    den = [Ti, 0.0]
    return num, den


def closed_loop(R_num, R_den, G_num, G_den):
    OL_num = mult(R_num, G_num)
    OL_den = mult(R_den, G_den)
    CL_num = OL_num
    CL_den = add(OL_den, OL_num)
    return CL_num, CL_den


# --- NOMINAL PARAMETERS ---
Kv = 0.8776
Tv = 4.9646
Lv = 0.8649

Kp2 = 3.2703
Ti2 = 4.9646

Kp = 1.2270
T1p = 5.9870
T2p = 5.9871
Lp = 3.9478

Kp1 = 1.2676
Ti1 = 11.9741
Td1 = 2.9935


# --- BUILD TRANSFER FUNCTIONS ---
Gv_num, Gv_den = fopdt(Kv, Tv, Lv)
R2_num, R2_den = pi_controller(Kp2, Ti2)
C2_num, C2_den = closed_loop(R2_num, R2_den, Gv_num, Gv_den)

Gp_num, Gp_den = sopdt(Kp, T1p, T2p, Lp)
Geq_num, Geq_den = Gp_num, Gp_den

R1_num, R1_den = pid_controller(Kp1, Ti1, Td1)
C1_num, C1_den = closed_loop(R1_num, R1_den, Geq_num, Geq_den)


# --- SIMULATE STEP RESPONSES ---
t_inner = np.linspace(0.0, 50.0, 2000)
sys_c2 = sig.TransferFunction(C2_num, C2_den)
_, y2_step = sig.step(sys_c2, T=t_inner)

t_outer = np.linspace(0.0, 60.0, 2000)
sys_c1 = sig.TransferFunction(C1_num, C1_den)
_, y1_step = sig.step(sys_c1, T=t_outer)


# --- PLOTTING CODE (ASCII labels/comments only) ---
fig, ax1 = plt.subplots(figsize=(10, 6))

# 1. Outer loop (pressure) - left Y axis (red)
color1 = '#D32F2F'
ax1.set_xlabel('Time (s)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Pressure (normalized, outer loop)', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(t_outer, y1_step, color=color1, linewidth=2.5, label='Step response y1(t) (pressure)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle=':', alpha=0.5)

# Create second Y axis (Y2)
ax2 = ax1.twinx()

# 2. Inner loop (flow) - right Y axis (blue)
color2 = '#1976D2'
ax2.set_ylabel('Flow (normalized, inner loop)', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(t_inner, y2_step, color=color2, linewidth=2.5, linestyle='--', label='Step response y2(t) (flow)')
ax2.tick_params(axis='y', labelcolor=color2)

# 3. Setpoint line (Setpoint = 1)
line3 = ax1.axhline(1.0, color='#2ECC71', linestyle=':', linewidth=2, label='Setpoint = 1')

# Combine legends
lines = line1 + line2 + [line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right', facecolor='white', edgecolor='lightgray')

plt.title('STEP RESPONSE OF INNER AND OUTER LOOPS', fontsize=13, fontweight='bold', pad=15)
plt.xlim(0, 60)
plt.tight_layout()

# Show
plt.show()