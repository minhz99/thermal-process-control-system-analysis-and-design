# Thermal Process Control System Analysis and Design

**Phân tích và tổng hợp hệ thống điều khiển quá trình nhiệt**

Đồ án / Bài tập lớn môn học: Phân tích và tổng hợp hệ thống điều khiển quá trình nhiệt.

## Giới thiệu
Dự án này tập trung vào phân tích và thiết kế hệ thống điều khiển cho quá trình nhiệt, cụ thể là **Hệ thống cấp nhiên liệu dầu (Fuel Oil Supply to Boiler System)**. 

Mục tiêu chính của hệ thống là:
1. Đảm bảo lưu lượng nhiên liệu (Flow) theo tải lò hơi.
2. Duy trì áp suất phun (Pressure) ổn định.
3. Gia nhiệt (Temperature) để nhiên liệu đạt độ nhớt phù hợp.
4. Đảm bảo tính liên tục và an toàn khi vận hành.

## Cấu trúc hệ thống điều khiển
Hệ thống bao gồm các vòng điều khiển (Control Loops) chính:
- **Flow Control (FIC)**: Điều khiển lưu lượng làm biến điều khiển chính dựa trên yêu cầu phụ tải của lò hơi (Boiler Master / Load demand).
- **Pressure Control (PIC)**: Ổn định áp suất phun qua van bypass để tối ưu hóa quá trình đốt.
- **Temperature Control (TIC)**: Vòng điều khiển gia nhiệt bằng hơi (steam) giúp giữ dầu FO ở nhiệt độ và độ nhớt tối ưu (110–140°C).
- **Level Control (LIC)**: Điều khiển mức các bể chứa (Tank 1 & 2) kết hợp với logic bảo vệ bơm.

## Cấu trúc thư mục
- `Chuong/`: Chứa mã nguồn LaTeX cho báo cáo chi tiết các chương.
- `Hinhve/`: Các hình ảnh, sơ đồ điều khiển và kết quả mô phỏng.
- `main.tex`: File LaTeX chính tổng hợp báo cáo.

## Thành viên
- Nhóm thực hiện: Nhóm 04

## Giấy phép (License)
Dự án được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.
