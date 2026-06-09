import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.signal as sig

def mult(p1, p2):
    return np.convolve(p1, p2)

def add(p1, p2):
    return np.polyadd(p1, p2)

# ============================================================
# Hàm truyền FOPDT: G(s) = K / (T*s + 1) * e^(-L*s)
# ============================================================
def fopdt(K, T, L):
    num0 = [K]
    den0 = [T, 1.0]
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)

# ============================================================
# Hàm truyền SOPDT: G(s) = K / ((T1*s + 1)(T2*s + 1)) * e^(-L*s)
# ============================================================
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

# ============================================================
# THÔNG SỐ TỪ VĂN BẢN
# ============================================================

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

# ============================================================
# XÂY DỰNG HÀM TRUYỀN
# ============================================================

Gv_num, Gv_den = fopdt(Kv, Tv, Lv)
R2_num, R2_den = pi_controller(Kp2, Ti2)
C2_num, C2_den = closed_loop(R2_num, R2_den, Gv_num, Gv_den)

Gp_num, Gp_den = sopdt(Kp_proc, T1p, T2p, Lp)
Geq_num, Geq_den = Gp_num, Gp_den
R1_num, R1_den = pid_controller(Kp1, Ti1, Td1)
C1_num, C1_den = closed_loop(R1_num, R1_den, Geq_num, Geq_den)

# ============================================================
# MÔ PHỎNG ĐÁP ỨNG XUNG (Impulse Response)
# Đáp ứng xung = đạo hàm đáp ứng bậc thang
# Hoặc dùng sig.impulse trên hàm truyền vòng kín
# ============================================================

t_inner = np.linspace(0.0, 50.0, 2000)
sys_c2 = sig.TransferFunction(C2_num, C2_den)
_, y2_step = sig.step(sys_c2, T=t_inner)

t_outer = np.linspace(0.0, 60.0, 2000)
sys_c1 = sig.TransferFunction(C1_num, C1_den)
_, y1_step = sig.step(sys_c1, T=t_outer)

dt = t_inner[1] - t_inner[0]
y2_impulse = np.gradient(y2_step, dt)
y1_impulse = np.gradient(y1_step, dt)

# ============================================================
# VẼ HÌNH
# ============================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.patch.set_facecolor('#f9f9f9')

# Vẽ đáp ứng xung với vùng đổi dấu
def plot_impulse(ax, t, y, color, label):
    ax.plot(t, y, color=color, linewidth=2.5, label=label)
    ax.axhline(0.0, color='#888888', linestyle='-', linewidth=1.0)
    ax.axvline(0.0, color='#888888', linestyle='-', linewidth=1.0)
    ax.fill_between(t, y, 0, where=(y >= 0), alpha=0.20, color=color)
    ax.fill_between(t, y, 0, where=(y < 0), alpha=0.20, color='#E74C3C')

# ---- Subplot 1: Vòng trong ----
plot_impulse(ax1, t_inner, y2_impulse, '#1976D2',
             r'Đáp ứng xung $y_2(t)$ (lưu lượng dầu)')
ax1.set_title('Đáp ứng xung vòng điều khiển lưu lượng dầu (Vòng trong)',
              fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel('Thời gian (s)', fontsize=11)
ax1.set_ylabel('Lưu lượng chuẩn hóa', fontsize=11)
ax1.set_xlim(0, 50)
ymax1 = np.max(np.abs(y2_impulse)) * 1.25
ax1.set_ylim(-ymax1, ymax1)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(fontsize=10, loc='upper right',
           facecolor='white', edgecolor='lightgray', framealpha=0.9)
ax1.set_facecolor('#fafafa')

textstr1 = (r'$K_v=0.8776,\;T_v=4.96s,\;L_v=0.86s$' + '\n'
            r'$K_{p2}=3.27,\;T_{i2}=4.96s$')
ax1.text(0.52, 0.82, textstr1, transform=ax1.transAxes,
         fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                   edgecolor='lightgray', alpha=0.9))

# ---- Subplot 2: Vòng ngoài ----
plot_impulse(ax2, t_outer, y1_impulse, '#D32F2F',
             r'Đáp ứng xung $y_1(t)$ (áp suất hơi)')

# Vẽ thêm đáp ứng xung vòng trong để so sánh (cùng hệ trục thời gian)
ax2_t = t_inner
ax2.plot(ax2_t, y2_impulse, color='#1976D2', linewidth=1.5, linestyle='-.',
         alpha=0.7, label=r'Đáp ứng xung vòng trong (tham chiếu)')

ax2.set_title('Đáp ứng xung vòng điều khiển áp suất hơi (Cascade vòng kín)',
              fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel('Thời gian (s)', fontsize=11)
ax2.set_ylabel('Áp suất hơi chuẩn hóa', fontsize=11)
ax2.set_xlim(0, 60)
ymax2 = np.max(np.abs(y1_impulse)) * 1.25
ax2.set_ylim(-ymax2, ymax2)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(fontsize=10, loc='upper right',
           facecolor='white', edgecolor='lightgray', framealpha=0.9)
ax2.set_facecolor('#fafafa')

textstr2 = (r'$K_p=1.227,\;T_{1p}=T_{2p}\approx5.99s,\;L_p=3.95s$' + '\n'
            r'$K_{p1}=1.27,\;T_{i1}=11.97s,\;T_{d1}=2.99s$')
ax2.text(0.38, 0.82, textstr2, transform=ax2.transAxes,
         fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                   edgecolor='lightgray', alpha=0.9))

plt.tight_layout(pad=2.5)

out_path = ("/Users/minhz/Desktop/HUST/KS/Phân tích và tổng hợp hệ thống điều khiển "
            "quá trình nhiệt/btl-dk/Hinhve/impulse_response.png")
plt.savefig(out_path, dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"Đã lưu: {out_path}")
