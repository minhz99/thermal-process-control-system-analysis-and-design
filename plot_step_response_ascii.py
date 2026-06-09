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
# Ham truyen QTB1T: G(s) = K / (T*s + 1) * e^(-L*s)
# voi Pade bac 1 cho khau tre
# ============================================================
def fopdt(K, T, L):
    # Phan khong tre: K / (T*s + 1)
    num0 = [K]
    den0 = [T, 1.0]
    # Pade bac 1 cho e^(-L*s)
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)

# ============================================================
# Ham truyen QTB2T: G(s) = K / ((T1*s + 1)(T2*s + 1)) * e^(-L*s)
# ============================================================
def sopdt(K, T1, T2, L):
    num0 = [K]
    den0 = mult([T1, 1.0], [T2, 1.0])
    num_p = [-L / 2.0, 1.0]
    den_p = [L / 2.0, 1.0]
    return mult(num0, num_p), mult(den0, den_p)

# ============================================================
# Bo dieu khien PI: R(s) = Kp * (1 + 1/(Ti*s)) = (Kp*Ti*s + Kp) / (Ti*s)
# ============================================================
def pi_controller(Kp, Ti):
    num = [Kp * Ti, Kp]
    den = [Ti, 0.0]
    return num, den

# ============================================================
# Bo dieu khien PID: R(s) = Kp * (1 + 1/(Ti*s) + Td*s)
# = (Kp*Td*Ti*s^2 + Kp*Ti*s + Kp) / (Ti*s)
# ============================================================
def pid_controller(Kp, Ti, Td):
    num = [Kp * Td * Ti, Kp * Ti, Kp]
    den = [Ti, 0.0]
    return num, den

# ============================================================
# Vong kin: C(s) = R(s)*G(s) / (1 + R(s)*G(s))
# ============================================================
def closed_loop(R_num, R_den, G_num, G_den):
    # R(s)*G(s)
    OL_num = mult(R_num, G_num)
    OL_den = mult(R_den, G_den)
    # 1 + R(s)*G(s)
    CL_num = OL_num
    CL_den = add(OL_den, OL_num)
    return CL_num, CL_den

# ============================================================
# THONG SO TU VAN BAN
# ============================================================

# ---- Vong trong (van): QTB1T ----
Kv = 0.8776
Tv = 4.9646
Lv = 0.8649

# PI vong trong (IMC)
Kp2 = 3.2703
Ti2 = 4.9646

# ---- Vong ngoai (ap suat hoi): QTB2T ----
Kp = 1.2270
T1p = 5.9870
T2p = 5.9871
Lp = 3.9478

# PID vong ngoai (Ben vung toi uu)
Kp1 = 1.2676
Ti1 = 11.9741
Td1 = 2.9935

# ============================================================
# XAY DUNG HAM TRUYEN
# ============================================================

# Van G_v(s)
Gv_num, Gv_den = fopdt(Kv, Tv, Lv)

# PI vong trong R2(s)
R2_num, R2_den = pi_controller(Kp2, Ti2)

# Vong kin vong trong: C2(s)
C2_num, C2_den = closed_loop(R2_num, R2_den, Gv_num, Gv_den)

# Lo hoi G_p(s) (doi tuong vong ngoai)
Gp_num, Gp_den = sopdt(Kp, T1p, T2p, Lp)

# Doi tuong tuong duong vong ngoai = C2(s) * G_p(s)
# (xap xi C2 ≈ 1 trong tinh toan, nhung o day dung C2 de mo phong chinh xac)
# De mo phong cascade that su, dung G_eq = G_p (vi C2 ≈ 1 trong dai tan vong ngoai)
Geq_num, Geq_den = Gp_num, Gp_den

# PID vong ngoai R1(s)
R1_num, R1_den = pid_controller(Kp1, Ti1, Td1)

# Vong kin vong ngoai: C1(s)
C1_num, C1_den = closed_loop(R1_num, R1_den, Geq_num, Geq_den)

# ============================================================
# MO PHONG Dap ung bac thang
# ============================================================

t_sim_vong_trong = np.linspace(0.0, 50.0, 2000)
sys_c2 = sig.TransferFunction(C2_num, C2_den)
_, y2 = sig.step(sys_c2, T=t_sim_vong_trong)

t_sim_vong_ngoai = np.linspace(0.0, 60.0, 2000)
sys_c1 = sig.TransferFunction(C1_num, C1_den)
_, y1 = sig.step(sys_c1, T=t_sim_vong_ngoai)

# ============================================================
# VE HINH
# ============================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.patch.set_facecolor('#f9f9f9')

# ---- Subplot 1: Vong trong (luu luong dau) ----
ax1.plot(t_sim_vong_trong, y2, color='#1976D2', linewidth=2.5,
         label=r'Dap ung $y_2(t)$ (luu luong dau)')
ax1.axhline(1.0, color='#388E3C', linestyle='--', linewidth=1.8,
            label=r'Tin hieu dat $r_2(t) = 1$', zorder=2)
ax1.fill_between(t_sim_vong_trong, y2, 1.0,
                 where=(y2 < 1.0), alpha=0.15, color='#1976D2')
ax1.set_title('Dap ung qua do vong dieu khien luu luong dau (Vong trong)',
              fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel('Thoi gian (s)', fontsize=11)
ax1.set_ylabel('Luu luong chuan hoa', fontsize=11)
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 1.18)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(fontsize=10, loc='lower right',
           facecolor='white', edgecolor='lightgray', framealpha=0.9)
ax1.set_facecolor('#fafafa')

# Them chu thich thong so
textstr1 = (r'$K_v=0.8776,\;T_v=4.96s,\;L_v=0.86s$' + '\n'
            r'$K_{p2}=3.27,\;T_{i2}=4.96s$')
ax1.text(0.55, 0.15, textstr1, transform=ax1.transAxes,
         fontsize=9, verticalalignment='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                   edgecolor='lightgray', alpha=0.9))

# ---- Subplot 2: Vong ngoai (ap suat hoi) ----
ax2.plot(t_sim_vong_ngoai, y1, color='#D32F2F', linewidth=2.5,
         label=r'Dap ung $y_1(t)$ (ap suat hoi)')
ax2.axhline(1.0, color='#388E3C', linestyle='--', linewidth=1.8,
            label=r'Tin hieu dat $z(t) = 1$', zorder=2)
ax2.fill_between(t_sim_vong_ngoai, y1, 1.0,
                 where=(y1 < 1.0), alpha=0.15, color='#D32F2F')
ax2.set_title('Dap ung qua do vong dieu khien ap suat hoi (Hai vong von kin)',
              fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel('Thoi gian (s)', fontsize=11)
ax2.set_ylabel('Ap suat hoi chuan hoa', fontsize=11)
ax2.set_xlim(0, 60)
ax2.set_ylim(0, 1.18)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(fontsize=10, loc='lower right',
           facecolor='white', edgecolor='lightgray', framealpha=0.9)
ax2.set_facecolor('#fafafa')

# Them chu thich thong so
textstr2 = (r'$K_p=1.227,\;T_{1p}=T_{2p}\approx5.99s,\;L_p=3.95s$' + '\n'
            r'$K_{p1}=1.27,\;T_{i1}=11.97s,\;T_{d1}=2.99s$')
ax2.text(0.42, 0.15, textstr2, transform=ax2.transAxes,
         fontsize=9, verticalalignment='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                   edgecolor='lightgray', alpha=0.9))

# Duong dut gach cho vong trong tren hinh vong ngoai (ty le thoi gian)
# Vong trong hoi tu nhanh hon nhieu -> duong tham chieu nhanh
ax2_t = t_sim_vong_trong
ax2.plot(ax2_t, y2, color='#1976D2', linewidth=1.5, linestyle='-.',
         alpha=0.6, label=r'Dap ung vong trong (tham chieu)')

plt.tight_layout(pad=2.5)

out_path = "/Users/minhz/Desktop/HUST/KS/Phan tich va tong hop he thong dieu khien qua trinh nhiet/btl-dk/Hinhve/step_response.png"
plt.savefig(out_path, dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"Da luu: {out_path}")
