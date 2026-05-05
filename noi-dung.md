CHƯƠNG 1: NGHIÊN CỨU QUÁ TRÌNH CÔNG NGHỆ	6
1. Tổng quan về hệ thống	6
1.1 Giới thiệu chung	6
1.2 Thành phần chính của hệ thống	6
1.3 Nguyên lý hoạt động	7
1.4 Phân loại hệ thống điều khiển lưu lượng dầu	7
2. Miêu tả sơ đồ công nghệ	7
3. Thiết kế sơ đồ công nghệ tổng quan	9
4. Vai trò của hệ thống	9
5. Thiết bị công nghệ chính của hệ thống điều khiển lưu lượng dầu trong nhà máy nhiệt điện	10
5.1. Thiết bị đo lường (Cảm biến lưu lượng)	10
5.2. Thiết bị chấp hành (Van điều khiển)	11
5.3. Thiết bị điều khiển (Bộ điều khiển)	12
5.4. Thiết bị phụ trợ và giám sát khác	12
CHƯƠNG 2: ĐO LƯỜNG / ĐIỀU KHIỂN	13
2.1 Các thiết bị đo lường trong hệ thống, các thông số được đo	13
2.2 Mạch vòng điều chỉnh hệ thống	14
2.3 Thiết kế, vẽ sơ đồ P&ID mạch vòng điều chỉnh chính của hệ thống:	15
2.3.1 Mạch vòng điều chỉnh nhiệt độ	15
2.3.2 Mạch vòng điều chỉnh lưu lượng và áp suất	15
2.3.3 Mạch vòng điều chỉnh mức	16
CHƯƠNG 3: TỔNG HỢP HỆ THỐNG ĐIỀU KHIỂN MỘT VÒNG	17
3.1 Nhận dạng hệ thống	17
3.2 Tính độ ĐK bền vững:	20
3.3 Đáp ứng quá độ của hệ thống	20
4.4 Chỉ tiêu chất lượng	22
CHƯƠNG 4: KẾT LUẬN	24

PHÂN CHIA CÔNG VIỆC
Nội dung	Phân chia
Mở đầu	Minh
1.1 Tổng quan về hệ thống	Hà
1.2 Miêu tả sơ đồ công nghệ	Hà
1.3 Thiết kế sơ đồ công nghệ tổng quan	Minh
1.4 Vai trò của hệ thống	Minh
1.5 Thiết bị công nghệ chính	Minh
2.1 Các thiết bị đo lường	Hà
2.2 Mạch vòng điều chỉnh hệ thống	Hà
2.3 Thiết kế sơ đồ P&ID	Hà
3.1 Nhận dạng hệ thống	Hà
3.2 Tính bộ điều khiển bền vững	Hà
3.3 Đáp ứng quá độ của hệ thống	Minh
3.4 Chỉ tiêu chất lượng	Minh
4. Kết luận	Minh


MỞ ĐẦU
Trong bối cảnh nhu cầu sử dụng điện năng ngày càng tăng cao, các nhà máy nhiệt điện vẫn đóng vai trò quan trọng trong việc đảm bảo nguồn cung năng lượng ổn định cho hệ thống điện quốc gia. Để duy trì hoạt động hiệu quả và liên tục của nhà máy nhiệt điện, việc quản lý và điều khiển các khâu trong quá trình sản xuất điện – đặc biệt là hệ thống nhiên liệu – đóng vai trò then chốt. Trong đó, hệ thống điều khiển lưu lượng dầu nhiên liệu giữ một vị trí hết sức quan trọng, ảnh hưởng trực tiếp đến hiệu suất cháy, mức tiêu hao nhiên liệu, độ ổn định vận hành của lò hơi, cũng như sự an toàn tổng thể của toàn bộ nhà máy.
Dầu nhiên liệu là một trong những dạng năng lượng đầu vào phổ biến tại các nhà máy nhiệt điện, đặc biệt là trong các hệ thống sử dụng lò đốt. Lưu lượng dầu được cấp vào buồng đốt cần được kiểm soát một cách chính xác theo từng thời điểm, phù hợp với tải tiêu thụ và điều kiện vận hành của tổ máy. Nếu lưu lượng dầu quá thấp, hiệu suất cháy sẽ giảm, dẫn đến tình trạng thiếu hơi, sụt áp và tổn thất nhiệt. Ngược lại, nếu cung cấp quá mức, sẽ gây ra tình trạng dư nhiên liệu, làm tăng tiêu hao không cần thiết, phát thải khí độc hại và nguy cơ mất an toàn cháy nổ.
Hệ thống điều khiển lưu lượng dầu nhiên liệu bao gồm nhiều phần tử kỹ thuật như cảm biến đo lưu lượng, cảm biến áp suất, cảm biến nhiệt độ, bộ truyền động, van điều khiển và bộ điều khiển trung tâm (có thể là bộ điều khiển logic khả trình - PLC hoặc hệ thống điều khiển phân tán - DCS). Hệ thống này đảm nhận vai trò thu thập dữ liệu từ hiện trường, xử lý thông tin, đưa ra tín hiệu điều khiển thích hợp nhằm duy trì lưu lượng dầu trong giới hạn tối ưu, bất kể điều kiện vận hành có thay đổi.
Nhiệm vụ của đề tài này là nghiên cứu, phân tích nguyên lý làm việc của hệ thống điều khiển lưu lượng dầu nhiên liệu trong nhà máy nhiệt điện; xây dựng mô hình điều khiển và mô phỏng quá trình vận hành; từ đó đánh giá khả năng đáp ứng của hệ thống cũng như đề xuất các giải pháp nâng cao hiệu quả điều khiển.
Mục đích của bài tập lớn nhằm giúp sinh viên hiểu rõ mối quan hệ giữa các tham số công nghệ trong hệ thống nhiệt điện, đặc biệt là vai trò của điều khiển tự động trong quá trình cung cấp và sử dụng nhiên liệu. Thông qua việc nghiên cứu thực tế và mô phỏng hệ thống điều khiển lưu lượng dầu, sinh viên có cơ hội rèn luyện kỹ năng tư duy hệ thống, phân tích kỹ thuật, lập trình điều khiển và thiết kế mô hình mô phỏng – những kỹ năng quan trọng đối với kỹ sư trong ngành công nghiệp năng lượng.
Ý nghĩa của đề tài không chỉ dừng lại ở góc độ học thuật hay giảng dạy, mà còn mang tính ứng dụng thực tiễn cao. Khi hệ thống điều khiển hoạt động hiệu quả, nhà máy có thể tiết kiệm đáng kể lượng nhiên liệu tiêu thụ, giảm chi phí sản xuất điện, đồng thời góp phần bảo vệ môi trường nhờ giảm thiểu phát thải khí CO₂, NOₓ và các hợp chất độc hại khác. Bên cạnh đó, việc đảm bảo điều khiển lưu lượng dầu chính xác và ổn định cũng là một trong những yếu tố quyết định đến tuổi thọ thiết bị và mức độ an toàn trong vận hành.
Với những lý do trên, việc nghiên cứu và xây dựng hệ thống điều khiển lưu lượng dầu nhiên liệu trong nhà máy nhiệt điện là một nội dung có tính thời sự và thiết thực, góp phần đáp ứng yêu cầu hiện đại hóa và tự động hóa trong ngành công nghiệp năng lượng.

CHƯƠNG 1: NGHIÊN CỨU QUÁ TRÌNH CÔNG NGHỆ
1.1 Tổng quan về hệ thống
1.1.1 Giới thiệu chung
Hệ thống điều khiển lưu lượng dầu nhiên liệu là một hệ thống quan trọng trong các nhà máy nhiệt điện, công nghiệp và hàng hải. Có vai trò quan trọng trong vận hành lò hơi, mục đích chính  của hệ thống điều khiển dầu nhiên liệu là điều chỉnh chính xác lượng dầu cấp vào buồng đốt để đảm bảo quá trình cháy ổn định, hiệu suất cao và an toàn cho quá trình đốt cháy.
 
Hình 1. Sơ đồ hệ thống điều khiển cấp dầu nhiên liệu

1.1.2 Thành phần chính của hệ thống
Bơm dầu nhiên liệu	Cung cấp dầu từ bể chứa đến vòi đốt với áp suất ổn định.
Van điều khiển lưu lượng	Điều chỉnh lưu lượng dầu dựa trên tín hiệu từ hệ thống điều khiển trung tâm.
Bộ lọc dầu	Loại bỏ tạp chất để tránh tắc nghẽn vòi phun.
Bộ gia nhiệt dầu	Giảm độ nhớt dầu (đặc biệt cần thiết với dầu FO nặng).
Hệ thống đo lường	Cảm biến lưu lượng, áp suất, nhiệt độ để giám sát liên tục.
Bộ điều khiển (PLC/DCS)	Xử lý tín hiệu và ra lệnh điều chỉnh van/bơm.

 1.1.3 Nguyên lý hoạt động
    Bơm dầu hút nhiên liệu từ bể chứa, đẩy qua hệ thống lọc và gia nhiệt.
    Lưu lượng kế đo lưu lượng thực tế, so sánh với giá trị đặt (setpoint) từ hệ thống điều khiển trung tâm (DCS).
    Bộ điều khiển (PID) tính toán sai lệch và điều chỉnh van tiết lưu hoặc tốc độ bơm để đạt lưu lượng mong muốn.
    Dầu được phun vào buồng đốt với áp suất và lưu lượng tối ưu, đảm    bảo cháy hoàn toàn.
1.1.4 Phân loại hệ thống điều khiển lưu lượng dầu
Loại hệ thống	Đặc điểm	Ứng dụng
Hệ thống hở	Dầu tuần hoàn một chiều, không tái sử dụng dầu thừa.	Nhà máy nhỏ, dầu nhẹ (DO).
Hệ thống kín	Dầu dư được hồi lưu về bể chứa, tiết kiệm nhiên liệu.	Nhà máy lớn, dầu nặng (FO).
Hệ thống tự động	Điều khiển bằng PLC/DCS, tích hợp với hệ thống giám sát lò hơi.	Nhà máy hiện đại.


 1.2 Miêu tả sơ đồ công nghệ
    Hệ thống điều khiển lưu lượng dầu nhiên liệu là thiết bị chính cung cấp dầu cấp vào buồng đốt để đảm bảo quá trình cháy ổn định, hiệu suất cao và an toàn cho quá trình đốt cháy.
    Dầu được bơm từ nguồn dầu vào bể đệm (buffer tank) sau đó được bơm vào các bể chứa 1 và 2 (tank 1,2) bằng các bơm dầu (Oil pump). Mức dầu trong các bể chứa được giám sát liên tục.
    Bơm dầu nhiên liệu ("FUEL OIL PUMP") hút dầu từ các bể chứa. Dầu sau bơm đi qua hệ thống gia nhiệt. Các thiết bị gia nhiệt sử dụng hơi nước (Steam pipe line) để tăng nhiệt độ của dầu lên mức phù hợp cho quá trình đốt. Việc gia nhiệt giúp giảm độ nhớt của dầu, cải thiện khả năng phun sương và cháy.
    Sau khi gia nhiệt, dầu được dẫn đến manifold phân phối dầu ("FUEL OIL SUPPLY"). Tại đây, dầu được chia thành các đường ống nhỏ hơn để cung cấp cho các nhóm đầu đốt khác nhau của lò hơi. 
    Lưu lượng dầu cung cấp đến từng nhóm đầu đốt được điều chỉnh bằng các van điều khiển. Áp suất dầu trong hệ thống được giám sát và duy trì ở mức cần thiết.
    Một phần dầu sau khi đi qua hệ thống gia nhiệt và trước khi đến các đầu đốt sẽ được hồi về ("Fuel-oil recirculation line"). Mục đích của đường hồi dầu là: Duy trì nhiệt độ ổn định cho dầu trong hệ thống, đặc biệt khi nhu cầu đốt thấp. Tránh tình trạng dầu bị quá nhiệt hoặc đóng cặn trong đường ống.
1.3 Thiết kế sơ đồ công nghệ tổng quan
 
Hình 2. Sơ đồ công nghệ tổng quan

1.4 Vai trò của hệ thống
    Điều tiết chính xác lượng nhiên liệu cấp vào lò hơi 
•  Giúp cung cấp đúng lưu lượng dầu theo nhu cầu tải của nhà máy
•  Đảm bảo quá trình cháy trong buồng đốt luôn diễn ra ổn định và hiệu quả.

    Tối ưu hóa hiệu suất đốt cháy và tiết kiệm nhiên liệu
•    Kết hợp với hệ thống điều khiển gió để duy trì tỷ lệ gió – nhiên liệu tối ưu.
•    Giảm tiêu hao nhiên liệu không cần thiết và nâng cao hiệu suất sinh hơ
    Đảm bảo an toàn vận hành hệ thống lò hơi
         •     Phản ứng nhanh với các tín hiệu áp suất, nhiệt độ và lưu lượng.
        •     Tự động điều chỉnh hoặc dừng cấp dầu khi xảy ra sự cố, tránh nguy cơ cháy nổ.
     .Tự động hóa và giám sát từ trung tâm điều khiển
•     Kết nối với PLC/DCS giúp điều khiển tự động, giám sát từ xa qua SCADA/HMI.
            •     Tạo điều kiện vận hành liên tục, chính xác và ít phụ thuộc vào thao tác thủ công.
- Giảm phát thải, bảo vệ môi trường
         •     Đốt cháy hiệu quả giúp hạn chế khói đen, muội than và khí độc (CO, NOx).
         •    Góp phần đáp ứng các tiêu chuẩn môi trường trong sản xuất điện năng.
1.5. Thiết bị công nghệ chính của hệ thống điều khiển lưu lượng dầu trong nhà máy nhiệt điện
1.5.1 Thiết bị đo lường (Cảm biến lưu lượng)
Chức năng chính của các thiết bị này là đo lường chính xác lượng dầu đang chảy qua đường ống và truyền tín hiệu về hệ thống điều khiển. Các loại cảm biến lưu lượng dầu phổ biến bao gồm:
    Đồng hồ đo lưu lượng dạng Coriolis: Cung cấp phép đo khối lượng dòng chảy trực tiếp với độ chính xác cao, ít bị ảnh hưởng bởi sự thay đổi về mật độ, nhiệt độ và độ nhớt của dầu.
    Đồng hồ đo lưu lượng dạng tuabin (Turbine meter): Sử dụng một rô-to quay tự do theo dòng chảy của dầu. Tốc độ quay của rô-to tỷ lệ thuận với tốc độ dòng chảy. Đây là lựa chọn phổ biến do chi phí hợp lý và dải đo rộng.
    Đồng hồ đo lưu lượng dạng bánh răng (Gear meter) hoặc bánh răng oval (Oval Gear meter): Thuộc loại đồng hồ đo lưu lượng thể tích, hoạt động dựa trên nguyên lý các bánh răng ăn khớp với nhau để "bắt" một lượng dầu nhất định trong mỗi vòng quay. Chúng phù hợp cho các loại dầu có độ nhớt khác nhau.
    Đồng hồ đo lưu lượng dựa trên chênh lệch áp suất (Differential Pressure Flow Meter): Hoạt động bằng cách tạo ra sự thu hẹp trong dòng chảy (ví dụ: sử dụng tấm orifice, ống Venturi, hoặc ống Pitot) và đo sự sụt áp qua điểm thu hẹp đó. Lưu lượng được tính toán dựa trên nguyên lý Bernoulli.
    Cảm biến lưu lượng siêu âm (Ultrasonic Flow Meter): Đo lưu lượng bằng cách truyền sóng siêu âm qua dòng chảy. Thời gian truyền sóng hoặc sự thay đổi tần số do hiệu ứng Doppler được sử dụng để xác định tốc độ dòng chảy.
Các nhà sản xuất phổ biến cho các thiết bị này bao gồm IFM, Alia, Digital Flow, Belimo, Krohne, Emerson, Yokogawa, Endress+Hauser.
1.5.2 Thiết bị chấp hành (Van điều khiển)
Van điều khiển là thiết bị cuối cùng trong vòng điều khiển, có nhiệm vụ điều chỉnh trực tiếp lưu lượng dầu đến các thiết bị sử dụng (ví dụ: lò hơi, tuabin) theo tín hiệu từ bộ điều khiển. Các loại van thường được sử dụng:
    Van cầu (Globe Valve): Thường được sử dụng cho các ứng dụng điều chỉnh lưu lượng do có khả năng điều tiết dòng chảy tốt.
    Van bi (Ball Valve): Có thể được sử dụng cho cả mục đích đóng/mở nhanh và điều tiết lưu lượng, tùy thuộc vào thiết kế của bi và cơ cấu chấp hành.
    Van bướm (Butterfly Valve): Thích hợp cho các đường ống có kích thước lớn và yêu cầu điều chỉnh lưu lượng ở mức độ nhất định.
    Van điện từ (Solenoid Valve): Thường dùng cho các ứng dụng đóng/mở nhanh, có thể được tích hợp vào các hệ thống an toàn hoặc các mạch điều khiển phụ trợ.
Các van này thường được vận hành bằng:
    Bộ truyền động điện (Electric Actuator): Sử dụng động cơ điện để điều khiển vị trí của van.
    Bộ truyền động khí nén (Pneumatic Actuator): Sử dụng áp lực khí nén để di chuyển cơ cấu chấp hành của van.
1.5.3 Thiết bị điều khiển (Bộ điều khiển)
Đây là "bộ não" của hệ thống, nhận tín hiệu từ các cảm biến lưu lượng, xử lý thông tin dựa trên các thuật toán điều khiển đã được lập trình (ví dụ: PID - Proportional Integral Derivative) và gửi tín hiệu điều khiển đến các van để duy trì lưu lượng dầu ở giá trị mong muốn (điểm đặt). Các thiết bị điều khiển chính bao gồm:
    Hệ thống điều khiển phân tán (DCS - Distributed Control System): Đây là hệ thống điều khiển toàn diện, thường được sử dụng trong các nhà máy lớn như nhà máy nhiệt điện. DCS cho phép điều khiển và giám sát tập trung toàn bộ các quy trình của nhà máy, bao gồm cả hệ thống dầu.
    Bộ điều khiển logic khả trình (PLC - Programmable Logic Controller): PLC được sử dụng rộng rãi để tự động hóa các quy trình công nghiệp. Trong hệ thống điều khiển lưu lượng dầu, PLC có thể thực hiện các logic điều khiển, xử lý tín hiệu và giao tiếp với các thiết bị khác.
    Hệ thống giám sát điều khiển và thu thập dữ liệu (SCADA - Supervisory Control and Data Acquisition): SCADA thường được sử dụng kết hợp với PLC hoặc DCS để cung cấp giao diện người-máy (HMI), cho phép người vận hành giám sát trạng thái hoạt động của hệ thống, xem các thông số (lưu lượng, áp suất, nhiệt độ), nhận cảnh báo và thực hiện các thao tác điều khiển thủ công nếu cần.
1.5.4 Thiết bị phụ trợ và giám sát khác
Ngoài các thiết bị chính kể trên, hệ thống còn có thể bao gồm:
    Cảm biến áp suất: Để giám sát áp suất dầu trong hệ thống.
    Cảm biến nhiệt độ: Để theo dõi nhiệt độ dầu, yếu tố có thể ảnh hưởng đến độ nhớt và tính chất của dầu.
    Bộ lọc dầu (Oil Filters): Loại bỏ cặn bẩn và tạp chất khỏi dầu để bảo vệ các thiết bị phía sau.
    Bơm dầu (Oil Pumps): Tạo ra áp lực cần thiết để vận chuyển dầu qua hệ thống.
    Van an toàn và van giảm áp: Bảo vệ hệ thống khỏi tình trạng quá áp.

CHƯƠNG 2: ĐO LƯỜNG / ĐIỀU KHIỂN
2.1 Các thiết bị đo lường trong hệ thống, các thông số được đo
     Lưu lượng kế (Flow Rate Transmitter – FT, FIC)
    Ký hiệu: FT, FIC
    Chức năng: Đo lưu lượng nhiên liệu (kg/h, m³/h...) hoặc nước.
    Thông số đo: Lưu lượng dòng chảy.
    Vị trí: Trên các đường ống dầu từ buffer tank đến bơm, sau bơm, đến lò hơi, và trên tuyến nước dịch vụ.
     Cảm biến mức (Level Transmitter – LT)
    Ký hiệu: LT, LIC, LL, L, H, HH
    Chức năng: Đo mức nhiên liệu trong các bồn chứa(Tank 1, Tank 2).
    Thông số đo: Mức chất lỏng trong bồn (theo % hoặc cm).
    Vị trí: Trên các bồn chứa nhiên liệu.
     Cảm biến áp suất (Pressure Transmitter – PT, PIC)
    Ký hiệu: PT, PIC, P>H
    Chức năng: Đo áp suất trong đường ống.
    Thông số đo: Áp suất làm việc (bar, psi...).
    Vị trí: Sau bơm, tại các điểm giao nhau và điều áp.
     Cảm biến nhiệt độ (Temperature Transmitter – TT)
    Ký hiệu: TT, TIC
    Chức năng: Đo nhiệt độ của dầu nhiên liệu hoặc nước.
    Thông số đo: Nhiệt độ (°C).
    Vị trí: Trên đường ống dẫn dầu nóng hoặc nước nóng.
     Van áp suất (Pressure Switch – PS)
    Ký hiệu: P>H, P<H
    Chức năng: Phát hiện áp suất vượt hoặc giảm quá mức cài đặt.
    Thông số đo: Áp suất
    Vị trí: Tại đầu ra của bơm, hoặc vị trí nguy cơ tăng áp.
2.2 Mạch vòng điều chỉnh hệ thống
 Hệ thống điều khiển cung cấp dầu nhiên liệu gồm nhiều mạch vòng điều chỉnh, trong đó gồm các mạch vòng điều khiển chính:
     Mạch vòng điều chỉnh nhiệt độ (TIC)
    Thiết bị đo: Cảm biến nhiệt độ (TT)
    Bộ điều khiển: TIC (Temperature Indicator Controller)
    Cơ cấu chấp hành: Van hơi vào bộ gia nhiệt (steam control valve)
    Chức năng: Giữ nhiệt độ dầu nhiên liệu ở mức phù hợp để đảm bảo độ nhớt thấp (dễ phun đốt).
    Ví dụ: Nếu nhiệt độ thấp → mở thêm van hơi → tăng nhiệt dầu.
     Mạch vòng điều chỉnh lưu lượng (FIC)
    Thiết bị đo: Lưu lượng kế (FT)
    Bộ điều khiển: FIC
    Cơ cấu chấp hành: Van điều chỉnh lưu lượng (FCV) hoặc biến tần của bơm
    Chức năng: Duy trì lưu lượng nhiên liệu cấp cho lò ổn định theo tải tiêu thụ.
     Mạch vòng điều chỉnh áp suất (PIC)
    Thiết bị đo: Cảm biến áp suất (PT)
    Bộ điều khiển: PIC
    Cơ cấu chấp hành: Van điều áp hoặc điều tốc bơm
    Chức năng: Đảm bảo áp suất dầu trong đường ống luôn ổn định, tránh hiện tượng sụt áp hoặc quá áp.
     Mạch vòng điều chỉnh mức (LIC)
    Thiết bị đo: Cảm biến mức (LT)
    Bộ điều khiển: LIC
    Cơ cấu chấp hành: Van nạp/xả dầu hoặc điều khiển bơm nạp
    Chức năng: Duy trì mức dầu ổn định trong các bồn chứa (Tank 1, Tank 2).

2.3 Thiết kế, vẽ sơ đồ PID mạch vòng điều chỉnh chính của hệ thống:
2.3.1 Mạch vòng điều chỉnh nhiệt độ
 
Hình 3. Sơ đồ điều chỉnh nhiệt độ
2.3.2 Mạch vòng điều chỉnh lưu lượng và áp suất 

 
Hình 4. Sơ đồ điều chỉnh lưu lượng và áp suất

2.3.3 Mạch vòng điều chỉnh mức

 
Hình 5. Sơ đồ điều chỉnh mức 








 
CHƯƠNG 3: TỔNG HỢP HỆ THỐNG ĐIỀU KHIỂN MỘT VÒNG
3.1 Nhận dạng hệ thống 
Khi tác động một xung đơn vị có dạng u(t) = 5,1.1(t) ta được đáp ứng ra y(t):
 
 


Xét đồ thị sau:
 
Tương ứng đồ thị:

 
Đối tượng quán tính có bậc quán tính bậc cao (≥2) có thể được mô tả chúng bằng một cách khá chính xác bằng mô hình quán tính bậc 2 có trễ.
Hàm truyền của đối tượng quán tính bậc hai có trễ 
O_((s))=(Ke^(-τ.s))/((1+T_1 s)(1+T_2 s))
Hàm quá độ :
                              h_M (t)=K〖.x〗_o.[1-T_1/(T_1-T_2 )×e^(-(t-τ)/T_1 )+T_2/(T_1-T_2 )×e^(-(t-τ)/T_2 )]
Dễ thấy, lưu lượng dầu làm đối tượng điều chỉnh có tự cần bằng điểm uốn của đường đặc tính không nằm trên trục hoành nên ta nhận dạng đối tượng theo khâu quán tính bậc 2 có trễ dạng K/(1+T_1 s)(1+T_2 s) .ⅇ^(-τs) bằng phương pháp kẻ-vẽ. Ta tiến hành nhận dạng đối tượng bằng xác định các tham số K (hệ số truyền), T_1,T_2 (hằng số quán tính) và τ (thời gian trễ) qua các bước: 

Bước 1: Kẻ đường tiếp tuyến đi qua điểm uốn U. Xác định các điểm A, B, C.
 
Từ đồ thị ta xác định được các thông số:
Điểm A (2.579;1,3), Điểm B (11,74;2,8)
Điểm C (11,744;1,3), Điểm U (6,2;1,88) 
y(∞)= 2,8 - 1,3 = 1,5 
y_u=1,88-1,3=0,58
t_u=6,2
T_AC=11,744-2,579= 9.165 
Bước 2: Xác định hệ số truyền K và độ cao tương đối của điểm uốn	
K = (y(∞))/u_0 =  1,5/5,1= 0,294
g = y_u/(y(∞))=0,58/1,5 = 0,386 > g_m=0,2642
Vậy đối tượng trên có điểm uốn cao
Bước 3: Xác định các tham số của đối tượng theo mô hình điểm uốn cao
Độ vượt ngưỡng: δ = g - g_m = 0,386 – 0,2642 = 0,1218
Hằng số quán tính: T_2 = T_1=  (T_AC (1-0,8δ))/e=(9.165 (1-0,8.0,1218))/e=3,04(s)
Thời gian trễ: τ= t_u-(T_AC (1+2,4δ))/e=6,2-9,165(1+2,4.0,1218)/e=1,84 (s) 
Vậy ta được bộ tham số của đối tượng: 
Hệ số truyền: K = 0,294
Thời gian quán tính: T_2 = T_1=3,04(s)
Thời gian trễ: τ=1,84(s)
Vậy hàm truyền đối tượng là O(s)=  0,294/〖(1+3,04s)〗^2 .e^(-1,84s)
3.2 Tính độ ĐK bền vững:
Xác định bộ điều chỉnh bền vững tối ưu R_1 cho vòng điều chỉnh áp suất theo chỉ tiêu tích phân bình phương sai số điều chỉnh của hệ bền vững đạt cực tiểu
I_min=∫▒〖ε^2 (t)dt=1,489〗
→{█(m_c=0,461@θ_c=1,348→θ=θ_c.τ=1,348.1,84=2,48)┤

→R_1=1/θs [O_PT (s)]^(-1)=1/2,48s.〖(1+3,04s)〗^2/0,294  = 1/2,48s.(9,2416s^2+6,08s+1)/0,294  =8,33+12,67s +  1,3715/s=8,33(1+1/6,073s+1,52s)

Hệ số truyền: K_p=8,33
Hằng số tích phân: T_i=6,073
Hằng số vi phân: T_d=1,52
3.3 Đáp ứng quá độ của hệ thống 
- Mô phỏng đáp ứng quá độ của hệ thống bằng Matlab ta có:

% Bước 1: Khai báo tham số hệ thống
K = 0.294;         % Hệ số khuếch đại
T = 3.04;          % Thời gian quán tính
L = 1,84;         % Thời gian trễ
% Bước 2: Tạo hàm truyền không trễ
s = tf(‘s’);
G_no_delay = K / (T*s + 1)^2;
% Bước 3: Gán thời gian trễ bằng xấp xỉ Pade bậc 1
G = G_no_delay * pade(exp(-L*s), 1);
% Bước 4: Vẽ đáp ứng xung
figure;
impulse(G, 30); % đáp ứng trong 30 giây
title(‘Đáp ứng xung của hệ thống’);
xlabel(‘Thời gian (s)’);
ylabel(‘Đáp ứng y(t)’);
grid on;
% Bước 5: Vẽ đáp ứng bậc thang (tùy chọn)
figure;
step(G, 30);
title(‘Đáp ứng bậc thang của hệ thống’);
xlabel(‘Thời gian (s)’);
ylabel(‘Đáp ứng y(t)’);
grid on;




- Kết quả mô phỏng: 
 
 

4.4 Chỉ tiêu chất lượng
- Thời gian quá độ: Ts ≈ 26s
- Biên độ đỉnh: 0,035
- Thời gian tác động: khoảng 4s
- Độ vọt:
O_s=((y_max-y_∞))/y_∞   ×100% ~ 21%
- Độ lệch tĩnh : Xấp xỉ 0.

 
CHƯƠNG 4: KẾT LUẬN
Trong chương này, hệ thống điều khiển lưu lượng dầu nhiên liệu trong giai đoạn khởi động lò hơi đã được nghiên cứu và tổng hợp theo phương pháp điều khiển một vòng. Dựa vào kết quả thu thập từ dữ liệu thực nghiệm và đồ thị đáp ứng quá độ, đối tượng được nhận dạng dưới dạng mô hình truyền đạt bậc nhất có trễ. Mô hình này phản ánh đúng đặc tính của hệ thống thực tế, bao gồm độ trễ khởi động và tính quán tính trong thay đổi lưu lượng dầu.
Trên cơ sở mô hình nhận dạng, bộ điều khiển PID đã được tính toán. Đây là phương pháp đơn giản nhưng hiệu quả trong việc thiết lập các tham số điều khiển ban đầu, đặc biệt với các hệ có mô hình quán tính bậc hai có trễ. Sau khi áp dụng, mô phỏng đáp ứng hệ thống cho thấy thời gian đáp ứng nhanh, dao động vừa phải và không có sai số ở trạng thái dừng. Độ vọt lố nằm trong giới hạn cho phép (khoảng 21%), thời gian quá độ và thời gian đạt đỉnh đều nằm trong phạm vi chấp nhận được cho giai đoạn khởi động lò.
Kết quả đạt được chứng minh rằng việc áp dụng mô hình hóa và thiết kế bộ điều khiển PID là hoàn toàn khả thi đối với hệ thống thực tế trong nhà máy nhiệt điện. Điều này không chỉ giúp đảm bảo an toàn khi khởi động mà còn góp phần tăng hiệu quả vận hành, giảm tổn thất năng lượng và bảo vệ thiết bị khỏi các tác động nhiệt – cơ bất thường. Phần tổng hợp điều khiển trong chương này là cơ sở quan trọng để bước sang các nội dung điều khiển nâng cao hơn hoặc điều khiển hai vòng trong các chương tiếp theo.

