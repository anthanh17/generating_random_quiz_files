Tưởng tượng bạn là giáo viên dạy Văn đang muốn dùng Python để tự động hoá
công việc. Sắp tới có một bài kiểm tra 15 phút và bạn cần soạn một bộ câu hỏi
cho học sinh trong lớp. Mỗi học sinh có một bộ câu hỏi dưới dạng.
```
Họ và tên:
Lớp:
--------------------------
Câu hỏi 1: Tác giả của Tuyên ngôn độc lập là ....
Câu hỏi 2: Tác giả của Tây tiến là ....


Câu hỏi 11: Ai là tác giả của Vợ chồng A Phủ?
A. Nguyên Huy Tưởng
B. Tô Hoài
C. Tố Hữu
D. Nguyễn Đình Thi

Câu hỏi 12: Ai là tác giả của Thuốc?
A. Lỗ Tấn
B. Tố Hữu
C. Tô Hoài
D. Chế Lan Viên
```
Mỗi bộ câu hỏi có 20 câu. 10 câu là câu hỏi điền từ, 10 câu là câu hỏi trắc nghiệm.
Mỗi cặp tác giả, tác phẩm chỉ được dùng trong 1 câu hỏi duy nhât. Thứ tự các câu có thể đảo lộn.
Thứ tự đáp án trong phần trắc nghiệm cũng cần phải được đảo lộn. Mỗi câu hỏi trắc nghiệm chỉ có một đáp án đúng. Các đáp án sai có thể điền tuỳ ý.
Với mỗi bộ câu hỏi, tạo một file đáp án có dạng
```
1. Hồ Chí Minh
2. Quang Dũng

11. B
12. A
```
Chú ý là đáp án tại mỗi câu trả lời cần phải ứng với câu hỏi tương ứng.
Tên của các file câu hỏi có dạng `bo_cau_hoi_1.txt`, `bo_cau_hoi_2.txt`, .... `1`, `2`, là số thứ tự của học sinh.
Tên của các file câu trả lời có dạng `dap_an_1.txt`, `dap_an_2.txt`, ....
Tất cả các file câu hỏi đặt trong thư mục `bo_cau_hoi`. Tất cả các file đáp án đặt trong thư mục `dap_an`.


**Khi nộp bài cần nộp cả code và hai thư mục `bo_cau_hoi` và `dap_an` trong đó có kèm theo các file được sinh ra.
Số học sinh mặc định là 10.**  
*Tham khảo project Generating Random Quiz Files*: https://automatetheboringstuff.com/2e/chapter9/
