Dưới đây là bản phân tích chi tiết cho toàn bộ thông số + logic điều khiển của hệ Fuel Oil Supply to Boiler System dựa trên HMI.

⸻

I. MỤC TIÊU HỆ THỐNG

Hệ thống cấp dầu FO có 4 mục tiêu điều khiển cốt lõi:

1. Đảm bảo lưu lượng nhiên liệu (Flow) theo tải lò
2. Duy trì áp suất phun ổn định
3. Gia nhiệt để đạt độ nhớt phù hợp
4. Đảm bảo tính liên tục & an toàn vận hành

⸻

II. PHÂN TÍCH CÁC NHÓM THÔNG SỐ

⸻

1. LƯU LƯỢNG (FLOW)

1.1 Thông số quan sát

* Total FO to Boiler: ~31883 (≈ 31.8 t/h)
* Các nhánh burner:
    * ~32.4 t/h
    * ~31.9 t/h
    * ~30.4 t/h

⸻

1.2 Ý nghĩa

* Đây là biến điều khiển chính (Primary Controlled Variable)
* Phản ánh trực tiếp:
    * Tải nhiệt của lò
    * Công suất phát điện

⸻

1.3 Cấu trúc điều khiển

Flow Control Loop (FIC):

* Input: FT (Flow Transmitter)
* Controller: PID
* Output:
    * Van điều khiển
    * Hoặc tốc độ bơm

⸻

1.4 Logic

* Setpoint từ:
    * Boiler Master / Load demand
* Có thể cascade:
    * Boiler Load → Fuel Flow

⸻

2. ÁP SUẤT (PRESSURE)

⸻

2.1 Thông số

* Trước burner: ~11–12 kgf/cm²
* Sau pump: ~48 kgf/cm²
* Low pressure side: ~0.7 kgf/cm²

⸻

2.2 Vai trò

* Quyết định chất lượng phun:
    * Áp thấp → giọt lớn → cháy kém
    * Áp cao → atomization tốt

⸻

2.3 Vòng điều khiển

Pressure Control Loop (PIC)

* Input: PT
* Output:
    * Van bypass (recirculation)
    * Hoặc speed pump

⸻

2.4 Logic điều khiển

* Nếu áp ↑:
    → mở bypass → giảm áp
* Nếu áp ↓:
    → đóng bypass → tăng áp

⸻

2.5 Interlock quan trọng

* Low Pressure:
    → Alarm
    → Trip burner (nếu nghiêm trọng)

⸻

3. NHIỆT ĐỘ (TEMPERATURE)

⸻

3.1 Thông số

* 79.6°C (trước heater)
* 109–140°C (sau heater)
* ~160°C (cục bộ)

⸻

3.2 Vai trò

FO có độ nhớt cao → cần gia nhiệt:

Nhiệt độ	Trạng thái
<100°C	quá đặc
110–140°C	tối ưu
>160°C	nguy hiểm

⸻

3.3 Vòng điều khiển

Temperature Control Loop (TIC)

* Input: TT
* Output: van steam heater

⸻

3.4 Logic

* Nếu T ↓:
    → mở steam valve
* Nếu T ↑:
    → đóng steam valve

⸻

3.5 Rủi ro

* Low T:
    → tắc nozzle
* High T:
    → phân hủy dầu

⸻

4. MỨC BỂ (LEVEL – TANK 1 & 2)

⸻

4.1 Thông số

* Tank 1: ~58.8%
* Tank 2: ~66.0%

⸻

4.2 Vai trò

* Buffer trung gian
* Tách khí / nước
* Ổn định hệ

⸻

4.3 Vòng điều khiển

Level Control Loop (LIC)

* Input: LT
* Output:
    * Van cấp
    * Pump transfer

⸻

4.4 Logic bảo vệ

Mức	Hành động
HH	đóng van cấp
LL	trip pump
LLL	shutdown hệ

⸻

5. BƠM (PUMPS)

⸻

5.1 Cấu hình

* 2 bơm: A/B
* Duty / Standby

⸻

5.2 Thông số

* Áp suất đầu ra
* Trạng thái ON/OFF

⸻

5.3 Logic điều khiển

Auto Mode:

* 1 bơm chạy
* 1 dự phòng

Failover:

* Pump A fail → Pump B start

⸻

5.4 Điều kiện Trip

* Low suction pressure
* Low level tank
* Overload

⸻

6. VAN (VALVES)

⸻

6.1 Phân loại

* Control valve
* Isolation valve
* Bypass valve

⸻

6.2 Trạng thái

* Xanh: mở
* Đỏ: đóng

⸻

6.3 Vai trò

* Điều chỉnh:
    * Flow
    * Pressure
    * Recirculation

⸻

7. TUẦN HOÀN (RECIRCULATION)

⸻

7.1 Chức năng

* Giữ dầu luôn nóng
* Tránh đóng cặn
* Ổn định áp suất

⸻

7.2 Logic

* Controlled by pressure loop
* Luôn mở một phần

⸻

8. HỆ GIA NHIỆT (STEAM SYSTEM)

⸻

8.1 Thành phần

* Steam line
* Heater coil

⸻

8.2 Điều khiển

* Van steam theo nhiệt độ

⸻

III. LOGIC ĐIỀU KHIỂN TỔNG THỂ

⸻

1. Chuỗi điều khiển chính

Boiler Load Demand
        ↓
Fuel Flow Setpoint
        ↓
Flow Controller (FIC)
        ↓
Valve / Pump
        ↓
Fuel to Burner

⸻

2. Cascade control

* Flow loop (primary)
* Pressure loop (secondary)
* Temperature loop (supporting)

⸻

3. Logic phối hợp

Biến	Vai trò
Flow	điều khiển chính
Pressure	ổn định phun
Temperature	đảm bảo độ nhớt
Level	đảm bảo nguồn

⸻

IV. LOGIC BẢO VỆ (INTERLOCK & TRIP)

⸻

1. Trip điều kiện

* Low FO pressure
* Low tank level
* Pump failure
* Low temperature
* No flow

⸻

2. Hành động

* Trip burner
* Stop pump
* Alarm operator

⸻

V. ĐÁNH GIÁ TRẠNG THÁI HỆ (TỪ HMI)

⸻

✔ Hệ đang vận hành ổn định:

* Flow cao (~31 t/h)
* Pressure ~11–12 kgf/cm² → đạt chuẩn
* Temperature ~120–140°C → tối ưu
* Tank level ~60% → an toàn

⸻

✔ Recirculation hoạt động

→ giảm dao động & ổn định nhiệt

⸻

VI. NHẬN XÉT KỸ THUẬT

⸻

Điểm tốt:

* Có đầy đủ vòng control
* Có redundancy (pump A/B)
* Có recirculation → thiết kế chuẩn

⸻

Điểm cần chú ý:

* Nhiệt độ có điểm lên ~160°C → cần kiểm tra
* Áp suất pump khá cao (~48 kgf/cm²) → cần giám sát seal

⸻

VII. KẾT LUẬN

Hệ thống là một multi-loop control system gồm:

* Primary loop: Flow control
* Secondary loops: Pressure + Temperature
* Support loops: Level + Pump logic

→ Đây là cấu trúc chuẩn công nghiệp cho FO boiler system
