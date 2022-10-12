#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
import os
from pathlib import Path

# The quiz data. Keys are works and values are their authors.
authors = {'Tuyên Ngôn Độc Lập': 'Hồ Chí Minh', 'Tây Tiến': 'Quang Dũng', 'Việt Bắc': 'Tố Hữu',
           'Đất Nước': 'Nguyễn Khoa Điềm', 'Tiếng Hát Con Tàu': 'Chế Lan Viên', 'Đò Lèn': 'Nguyễn Duy',
           'Sóng': 'Xuân Quỳnh', 'Đàn Ghi-ta-lor-ca': 'Thanh Thảo', 'Người Lái Đò Sông Đà': 'Nguyễn Tuân',
           'Ai Đặt Tên Cho Dòng Sông': 'Nguyễn Huy Tưởng', 'Vợ Chồng A Phủ': 'Tô Hoài',
           'Vợ Nhặt': 'Kim Lân', 'Rừng Xà Nu': 'Nguyễn Trung Thành', 'Những Đứa Con Trong Gia Đình': 'Nguyễn Thi',
           'Chiếc Thuyền Ngoài Xa': 'Nguyễn Minh Châu', 'Hồn Trương Ba, Da Hàng Thịt': 'Lưu Quang Vũ',
           'Dọn Về Làng': 'Nông Quốc Chấn', 'Thuốc': 'Lỗ Tấn', 'Số Phận Con Người': 'Sô-lô-khôp',
           'Ông Già Và Biển Cả': 'E. Hê-minh-uê'
           }


def generate_quiz_files(num_students: int = 10):
    ques_path = Path('bo_cau_hoi/')
    if not ques_path.exists():
        os.mkdir(ques_path)

    ans_path = Path('dap_an/')
    if not ans_path.exists():
        os.mkdir(ans_path)

    for filepath in ques_path.glob('*'):
        filepath.unlink()

    for filepath in ans_path.glob('*'):
        filepath.unlink()

    for i in range(num_students):
        ques_file = open(Path('bo_cau_hoi') / f'bo_cau_hoi_{i + 1}.txt', "w")
        ans_file = open(Path('dap_an') / f'dap_an_{i + 1}.txt', "w")
        ques_file.write("Họ và tên:\nLớp:\n----------------------------------------------------------------\n\n")

        ## list tac pham
        list_literaries = list(authors.keys())

        ## list tac gia
        list_authors = list(authors.values())

        list_questions = []
        list_questions = random.sample(list_literaries, 20)

        ## len(list_questions) = 20
        for j in range(len(list_questions)):
            if j < 10:
                ques_file.write(f"Câu hỏi {j + 1}: Tác giả của {list_questions[j]} là ....\n")
                ans_file.write(f"{j + 1}. {authors[list_questions[j]]}\n")
            else:
                ques_file.write(f"Câu hỏi {j + 1}: Ai là tác giả của {list_questions[j]}?\n")

                # # ans: list chứa 4 đáp án, lúc đầu chỉ có đáp án đúng.
                ans = [authors[list_questions[j]]]

                # # tao list moi
                # new_authors = list_authors[:]

                # # xoa dap an dung
                # new_authors.remove(authors[list_questions[j]])

                # # chon ra 3 cai ngau nhien
                # ans.extend(random.sample(new_authors, 3))

                # list_authors: A B C D E F G

                # A
                # A
                # B
                # D

                for ans_num in range(3):
                    while True:
                        author = random.choice(list_authors)
                        if author not in ans:
                            ans.append(author)
                            break
                
                random.shuffle(ans)

                # len(ans) = 4
                for ans_num in range(len(ans)):
                    choice = ""
                    match ans_num:
                        case 0:
                            choice = "A"
                        case 1:
                            choice = "B"
                        case 2:
                            choice = "C"
                        case 3:
                            choice = "D"
                    ques_file.write(f"{choice}. {ans[ans_num]}\n")
                    if ans[ans_num] == authors[list_questions[j]]:
                        ans_file.write(f"{j + 1}. {choice}\n")
            ques_file.write(f"\n")
        ans_file.close()
        ques_file.close()

generate_quiz_files(10)