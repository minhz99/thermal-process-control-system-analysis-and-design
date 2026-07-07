import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

def mult(p1, p2):
    return np.convolve(p1, p2)

def add(p1, p2):
    return np.polyadd(p1, p2)

st.set_page_config(page_title="Mô phỏng Hệ Điều Khiển Nối Tiếp", layout="wide")

st.title("Mô phỏng Cascade (BTL HE5092 - VĐ Minh & PN Hà)")
st.markdown("""
Giao diện này cho phép thay đổi thông số đặc tính của đối tượng và bộ điều khiển vòng trong / vòng ngoài 
để quan sát đáp ứng quá độ của hệ thống.
""")

# ---- Sidebar cho việc nhập tham số ----
st.sidebar.header("Thông số Vòng trong (Lưu lượng)")
st.sidebar.subheader("Đối tượng QTB1T")
K2 = st.sidebar.number_input("Hệ số khuếch đại (K2)", value=0.8836, format="%.4f", step=0.1) # 1.4137/1.6
T2 = st.sidebar.number_input("Hằng số thời gian (T2)", value=4.8694, format="%.4f", step=0.1)
L2 = st.sidebar.number_input("Thời gian trễ (L2)", value=0.8213, format="%.4f", step=0.1)

st.sidebar.header("Thông số Vòng ngoài (Áp suất)")
st.sidebar.subheader("Đối tượng QTB2T")
K1 = st.sidebar.number_input("Hệ số khuếch đại (K1)", value=1.2147, format="%.4f", step=0.1)
T1 = st.sidebar.number_input("Hằng số thời gian (T1)", value=6.0356, format="%.4f", step=0.1)
L1 = st.sidebar.number_input("Thời gian trễ (L1)", value=4.0457, format="%.4f", step=0.1)

st.sidebar.divider()

st.sidebar.subheader("Bộ điều khiển PID (R1)")
Kp1 = st.sidebar.number_input("Hệ số khuếch đại (Kp1)", value=1.8222, format="%.4f", step=0.1)
Ti1 = st.sidebar.number_input("Hằng số tích phân (Ti1)", value=12.0712, format="%.4f", step=0.1)
Td1 = st.sidebar.number_input("Hằng số vi phân (Td1)", value=3.0178, format="%.4f", step=0.1)

st.sidebar.subheader("Bộ điều khiển PI (R2)")
Kp2 = st.sidebar.number_input("Hệ số khuếch đại (Kp2)", value=4.9780, format="%.4f", step=0.1)
Ti2 = st.sidebar.number_input("Hằng số tích phân (Ti2)", value=4.8694, format="%.4f", step=0.1)

st.sidebar.divider()

st.sidebar.header("Cài đặt thời gian mô phỏng")
t_sim_inner = st.sidebar.number_input("Thời gian mô phỏng vòng trong (s)", value=30.0, step=5.0)
t_sim_outer = st.sidebar.number_input("Thời gian mô phỏng toàn mạch (s)", value=80.0, step=10.0)

# ---- Hàm tính toán mô phỏng ----
def simulate():
    # VÒNG TRONG
    num_v0 = [K2]
    den_v0 = [T2, 1.0]

    # Xấp xỉ Pade bậc 1 cho thời gian trễ L2
    if L2 > 0:
        num_p2 = [-L2 / 2.0, 1.0]
        den_p2 = [L2 / 2.0, 1.0]
    else:
        num_p2 = [1.0]
        den_p2 = [1.0]

    num_v = mult(num_v0, num_p2)
    den_v = mult(den_v0, den_p2)

    # Bộ điều khiển PI vòng trong R2
    num_r2 = [Kp2 * Ti2, Kp2]
    den_r2 = [Ti2, 0.0]

    # Hàm truyền vòng hở vòng trong
    num_o2 = mult(num_r2, num_v)
    den_o2 = mult(den_r2, den_v)
    
    # Hàm truyền vòng kín vòng trong
    num_c2 = num_o2
    den_c2 = add(den_o2, num_o2)

    # VÒNG NGOÀI
    num_b0 = [K1]
    den_b0 = mult([T1, 1.0], [T1, 1.0])

    # Xấp xỉ Pade bậc 1 cho thời gian trễ L1
    if L1 > 0:
        num_p1 = [-L1 / 2.0, 1.0]
        den_p1 = [L1 / 2.0, 1.0]
    else:
        num_p1 = [1.0]
        den_p1 = [1.0]

    num_b = mult(num_b0, num_p1)
    den_b = mult(den_b0, den_p1)

    # Hàm truyền đối tượng tương đương (Vòng trong kín nối tiếp với Đối tượng vòng ngoài)
    num_be = mult(num_c2, num_b)
    den_be = mult(den_c2, den_b)

    # Bộ điều khiển PID vòng ngoài R1
    num_r1 = [Kp1 * Td1 * Ti1, Kp1 * Ti1, Kp1]
    den_r1 = [Ti1, 0.0]

    # Hàm truyền vòng hở toàn mạch
    num_o1 = mult(num_r1, num_be)
    den_o1 = mult(den_r1, den_be)
    
    # Hàm truyền vòng kín toàn mạch
    num_c1 = num_o1
    den_c1 = add(den_o1, num_o1)

    # Mô phỏng quá độ
    t_sim2_arr = np.linspace(0.0, t_sim_inner, 600)
    sys_closed2 = sig.TransferFunction(num_c2, den_c2)
    t2, y2 = sig.step(sys_closed2, T=t_sim2_arr)

    t_sim1_arr = np.linspace(0.0, t_sim_outer, 800)
    sys_closed1 = sig.TransferFunction(num_c1, den_c1)
    t1, y1 = sig.step(sys_closed1, T=t_sim1_arr)

    return (t2, y2), (t1, y1)

# Nút chạy mô phỏng
if st.button("Chạy mô phỏng", type="primary"):
    with st.spinner("Đang tính toán đáp ứng quá độ..."):
        try:
            (t2, y2), (t1, y1) = simulate()
            
            # Vẽ biểu đồ chồng
            fig, ax1 = plt.subplots(figsize=(10, 6))

            color1 = '#d62728'
            ax1.set_xlabel('Thời gian (s)', fontsize=12, fontweight='bold')
            ax1.set_ylabel('Áp suất hơi chuẩn hóa (Vòng ngoài)', color=color1, fontsize=12, fontweight='bold')
            line1, = ax1.plot(t1, y1, color=color1, linewidth=2.5, label=r'Đáp ứng $y_1(t)$ (áp suất hơi)')
            ax1.tick_params(axis='y', labelcolor=color1)
            ax1.set_xlim(0, max(t_sim_inner, t_sim_outer))
            
            # Tính giới hạn y động để đồ thị không bị cắt
            y_max = max(np.max(y1), np.max(y2), 1.1)
            y_min = min(np.min(y1), np.min(y2), -0.1)
            pad = (y_max - y_min) * 0.05
            y_lim_bottom, y_lim_top = y_min - pad, y_max + pad
            
            ax1.set_ylim(y_lim_bottom, y_lim_top)

            ax2 = ax1.twinx()
            color2 = '#1f77b4'
            ax2.set_ylabel('Lưu lượng dầu chuẩn hóa (Vòng trong)', color=color2, fontsize=12, fontweight='bold')
            line2, = ax2.plot(t2, y2, color=color2, linewidth=2.5, linestyle='--', label=r'Đáp ứng $y_2(t)$ (lưu lượng dầu)')
            ax2.tick_params(axis='y', labelcolor=color2)
            ax2.set_ylim(y_lim_bottom, y_lim_top)

            line3 = ax1.axhline(1.0, color='#2ca02c', linestyle=':', linewidth=2.0, label='Tín hiệu đặt mục tiêu = 1')

            ax1.set_title("ĐỒ THỊ ĐÁP ỨNG QUÁ ĐỘ CỦA VÒNG TRONG VÀ VÒNG NGOÀI", fontsize=14, fontweight='bold', pad=15)
            ax1.grid(True, linestyle=":", alpha=0.6)

            lines = [line1, line2, line3]
            labels = [l.get_label() for l in lines]
            ax1.legend(lines, labels, loc='lower right', fontsize=11, framealpha=1)

            fig.tight_layout()
            st.pyplot(fig)
                
            st.success("Mô phỏng thành công!")
            
        except Exception as e:
            st.error(f"Đã xảy ra lỗi trong quá trình tính toán: {e}")
