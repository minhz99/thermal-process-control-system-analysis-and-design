import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.signal as sig


def mult(p1, p2):
    return np.convolve(p1, p2)


def add(p1, p2):
    return np.polyadd(p1, p2)


# Transfer function FOPDT: G(s)=K/(T*s+1)*e^(-L*s)
def fopdt(K, T, L):
    num0 = [K]
    den0 = [T, 1.0]
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)


# Transfer function SOPDT: G(s)=K/((T1*s+1)(T2*s+1))*e^(-L*s)
def sopdt(K, T1, T2, L):
    num0 = [K]
    den0 = mult([T1, 1.0], [T2, 1.0])
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)


def pi_controller(Kp, Ti):
    return [Kp * Ti, Kp], [Ti, 0.0]


def pid_controller(Kp, Ti, Td):
    return [Kp * Td * Ti, Kp * Ti, Kp], [Ti, 0.0]


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

Kp_proc = 1.2270
T1p = 5.9870
T2p = 5.9871
Lp = 3.9478
Kp1 = 1.2676
Ti1 = 11.9741
Td1 = 2.9935


# --- BUILD NOMINAL TRANSFER FUNCTIONS ---
Gv_num, Gv_den = fopdt(Kv, Tv, Lv)
R2_num, R2_den = pi_controller(Kp2, Ti2)
C2_num, C2_den = closed_loop(R2_num, R2_den, Gv_num, Gv_den)

Gp_num, Gp_den = sopdt(Kp_proc, T1p, T2p, Lp)
Geq_num, Geq_den = Gp_num, Gp_den
R1_num, R1_den = pid_controller(Kp1, Ti1, Td1)
C1_num, C1_den = closed_loop(R1_num, R1_den, Geq_num, Geq_den)


# --- SIMULATE IMPULSE RESPONSES ---
t_inner = np.linspace(0.0, 50.0, 2000)
sys_c2 = sig.TransferFunction(C2_num, C2_den)
_, y2_step = sig.step(sys_c2, T=t_inner)

t_outer = np.linspace(0.0, 60.0, 2000)
sys_cl = sig.TransferFunction(C1_num, C1_den)
_, y1_step = sig.step(sys_cl, T=t_outer)

dt = t_inner[1] - t_inner[0]
y2_impulse = np.gradient(y2_step, dt)
y1_impulse = np.gradient(y1_step, dt)


# --- PLOTTING CODE (ASCII labels/comments only) ---
fig, ax1 = plt.subplots(figsize=(10, 6))

# Horizontal zero line
ax1.axhline(0.0, color="#888888", linestyle='-', linewidth=1.0)

# 1. Plot outer loop (pressure) - left Y axis (red)
color1 = '#D32F2F'
ax1.set_xlabel('Time (s)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Pressure (normalized, outer loop)', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(t_outer, y1_impulse, color=color1, linewidth=2.5, label='Impulse response y1(t) (pressure)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle=':', alpha=0.5)

# Limit left axis to -0.6..0.6
ax1.set_ylim(-0.6, 0.6)

# Fill area for outer loop
ax1.fill_between(t_outer, y1_impulse, 0, where=(y1_impulse >= 0), alpha=0.15, color=color1)
ax1.fill_between(t_outer, y1_impulse, 0, where=(y1_impulse < 0), alpha=0.15, color='#E74C3C')

# Create second Y axis (inner loop)
ax2 = ax1.twinx()

# 2. Plot inner loop (flow) - right Y axis (blue)
color2 = '#1976D2'
ax2.set_ylabel('Flow (normalized, inner loop)', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(t_inner, y2_impulse, color=color2, linewidth=2, linestyle='-.', alpha=0.8, label='Impulse response y2(t) (flow)')
ax2.tick_params(axis='y', labelcolor=color2)

# Limit right axis to -0.6..0.6
ax2.set_ylim(-0.6, 0.6)

# Fill area for inner loop
ax2.fill_between(t_inner, y2_impulse, 0, where=(y2_impulse >= 0), alpha=0.1, color=color2)

# Combine legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', facecolor='white', edgecolor='lightgray')

plt.title('IMPULSE RESPONSE OF TWO-LOOP CONTROL SYSTEM', fontsize=13, fontweight='bold', pad=15)
plt.xlim(0, 60)
plt.tight_layout()

# Show
plt.show()