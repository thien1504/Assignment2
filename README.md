# Assignment2

 Tên dự án: Tính toán và phân tích điểm thi (Test Grade Calculator)
 Chương trình được viết bởi ngôn ngữ Python
 Chương trình được viết để tính toán điểm thi cho nhiều lớp với sĩ số hàng ngàn học sinh
 
## Input
 Input của chương trình là các file .txt có lưu mã học sinh và câu trả lời
 Mã học sinh được lưu theo format gồm 9 kí tự (Kí tự N viết liền theo sau đó là 8 chữ số) VD: N12345678 
 Câu trả lời gồm 25 câu với các đáp án có thể chọn là : A,B,C,D và rỗng (không chọn).
 ![image](https://user-images.githubusercontent.com/68512088/188257430-b48777eb-3939-4f3e-9e4b-659b11abf905.png)
 
## Output
 Chương trình sẽ xử lí loại bỏ các học sinh có mã học sinh không hợp lệ, có dư hoặc thiếu câu trả lời\n
 Người dùng cần tạo file câu trả lời trước khi chạy chương trình, khi nhập tên file không hợp lệ chương trình sẽ báo lỗi
 Chương trình thực hiện: 
     - Chấm điểm theo một list answer_key có sẵn
     - Thống kê tính toán các thông kê như: Mean (điểm trung bình của 1 lớp đó), Range, Câu hỏi bị bỏ qua nhiều nhất, ...
     - Tạo ra một file .txt lưu điểm cho từng học sinh 

![image](https://user-images.githubusercontent.com/68512088/188257674-0a0fd993-d291-4068-91d2-144d547eca9c.png)
Ngoài ra chương trình sẽ tạo file .txt valid_data lưu các data đạt chuẩn để thực hiện chấm điểm

## Usage
 Chạy cmd trong thư mục: 
  Nhập: python lastname_firstname_grade_the_exams.py
  => Enter class to grade: => Nhập tên file cần chấm điểm
  
![image](https://user-images.githubusercontent.com/68512088/188257952-a5560e43-4219-4b6f-943a-924a0986805d.png)

 

 
 
 
