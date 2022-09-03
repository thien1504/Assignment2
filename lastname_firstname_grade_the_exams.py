#Import library
import pandas as pd
import time
import sys

'''Có 2 trường hợp line sẽ invalid
	TH1: ID của học sinh sai (len(ID) không bằng 9)
	TH2: Học sinh trả lời thiếu hoặc dư
=> Tạo ra 2 list để lưu lại các trường hợp này và 1 list cho valid data
'''

list_invalid_id = []
list_valid_grade = []
list_invalid_answer = []

# Hàm lọc ra các học sinh có mã học sinh sai (Input là text file, output là 1 list)
def invalid_ID (text_file):
	list_invalid_id = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if len(line.split(",")[0]) != 9:
				list_invalid_id.append(line)
	return list_invalid_id

# Hàm lọc ra các học sinh có dư hoặc thiếu câu trả lời
def invalid_answer(text_file):
	list_invalid_answer = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if len(line.split(",")) != 26:
				list_invalid_answer.append(line)
	return list_invalid_answer

# Hàm lọc ra các data valid
def valid_grade(text_file, list_invalid_id, list_invalid_answer):
	# Tạo 1 list tổng chứa tất cả các học sinh
	list_valid_grade = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			list_valid_grade.append(line)

	#Lọc ra các valid data từ việc Xóa các invalid data trong list tổng
	for index, item in enumerate(list_valid_grade):
		if item in list_invalid_id or item in list_invalid_answer:
			list_valid_grade.pop(index)

	return list_valid_grade


#Main
text_file = input("Enter a class file to grade: ")

try:
	with open(f"{text_file}.txt") as fh:
		print(f"\nSuccessfully opened {text_file}.txt")
except:
	raise ("File cannot be found.")	

list_invalid_id = invalid_ID(text_file)
list_invalid_answer = invalid_answer(text_file)
list_valid_grade = valid_grade(text_file, list_invalid_id, list_invalid_answer)

# Valid line sẽ bằng số dòng của list valid data
valid_line = len(list_valid_grade)
# Số dòng invalid bằng tổng 2 list invalid data
invalid_line = len(list_invalid_id) + len(list_invalid_answer)

print("**** ANALYZING ****\n")
time.sleep(1)
if invalid_line == 0:
	print("No errors found!\n")
	print("**** REPORT ****")
	print(f"Total valid lines of data: {valid_line}")
	print("Total invalid lines of data: 0 ")
else:
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if line in list_invalid_id:
				print("Invalid line of data: N# is invalid")
				print(line)
			elif line in list_invalid_answer:
				print("Invalid line of data: does not contain exactly 26 values:")
				print(line)
	print("\n**** REPORT ****")
	print(f"Total valid lines of data: {valid_line}")
	print(f"Total invalid lines of data: {invalid_line}")

#Tạo file txt lưu những valid data
with open(f"{text_file}_valid_data.txt", "w") as fh:
	for i in list_valid_grade:
		fh.write(i)

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

#Tạo data frame csv từ file txt valid data, header = None để không lấy dòng đầu tiên làm tên cột
df = pd.read_csv(f"{text_file}_valid_data.txt", header = None, index_col = 0)

# Data Frame truoc khi cham diem
#             1    2    3    4    5    6    7  8    9    10   11   12   13   14   15   16   17 18   19   20   21   22   23   24   25
#0
#N00000001    A    A    D    D    C    D    D  A  NaN    C    D    B    C  NaN    B    C    B  D    A    C  NaN    A  NaN    C    D
#N00000002  NaN    A  NaN    D  NaN    B    D  A    C    C    D  NaN    A    A    A    C    B  D    C    C    A    A    B  NaN    D

#Hàm tính điểm cho 1 học sinh, Input là list answer key và list câu trả lời của học sinh đó
#Output là 1 list với các điểm tương ứng câu trả lời
#Nếu không trả lời thì +0 điểm, trả lời đúng +4, trả lời sai -1
def grading(list_answer_key, list_need_grade):
	for i in range(len(list_answer_key)):
		if list_need_grade[i] == list_answer_key[i]:
			list_need_grade[i] = 4
		elif list_need_grade[i] in ["A", "B", "C", "D"]:
			list_need_grade[i] = -1
		else:
			list_need_grade[i] = 0

	return list_need_grade

list_answer_key = list(answer_key.split(","))

#Apply điểm vào data frame
#Duyệt qua từng dòng của DataFrame, Apply hàm tính điểm và Overwrite lại vào DataFrame
for i in range(valid_line):
	df.iloc[i] = grading(list_answer_key, list(df.iloc[i]))

# Data Frame sau khi cham diem
#           1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16 17  18  19  20 21  22  23  24  25
#0
#N00000001  -1   4   4   4   4  -1   4   4   0   4   4   4  -1   0  -1   4  4   4   4   4  0   4   0  -1   4
#N00000002   0   4   0   4   0   4   4   4   4   4   4   0   4  -1   4   4  4   4  -1   4  4   4   4   0   4

#Duyệt qua từng dòng DataFrame và tính sum sau đó thêm vào list_grade
list_grade = []
for i in range(valid_line):
	list_grade.append(df.iloc[i].sum())

#Tạo cột Grade bằng với list_grade
df["Grade"] = list_grade

#DataFrame sau khi có cột điểm (Grade)
#            1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16 17  18  19  20 21  22  23  24  25  Grade
#0
#N00000001  -1   4   4   4   4  -1   4   4   0   4   4   4  -1   0  -1   4  4   4   4   4  0   4   0  -1   4     59
#N00000002   0   4   0   4   0   4   4   4   4   4   4   0   4  -1   4   4  4   4  -1   4  4   4   4   0   4     70

print("\nTotal student of high scores:",len(df[df["Grade"] > 80]) )
print("Mean (average) score:",df["Grade"].mean())
print("Highest score:",df["Grade"].max())
print("Lowest score:",df["Grade"].min())
print("Range of scores:",df["Grade"].max() - df["Grade"].min())
print("Median score:",df["Grade"].median())


#Hàm trả về số câu trả lời max theo biến num
#Input là data frame và num . Với num = 0 (Số câu trả lời bị skip), num = -1 (Số câu trả lời sai), num = 4(Số câu trả lời đúng)
def max_question(data_frame, num):
	max_question = 0
	for i in range(1,26):
		if len(df[df[i] == num]) > max_question:
			max_question = len(df[df[i] == num])
	return max_question

#Duyệt vòng lặp qua từng cột của dataframe 
#Thỏa mãn điều điện có số câu skip hoặc sai = với số câu max (Tính bằng hàm max_question)
#Từ đó lấy ra được vị trí cột, số người trả lời skip(hoặc sai) bằng hàm len => Từ đó tính đươc tỉ lệ
sys.stdout.write("Question that most people skip: ")
for i in range(1,26):
	if len(df[df[i] == 0]) == max_question(df, 0):
		sys.stdout.write(f"{i} - {max_question(df, 0)} - {max_question(df, 0) / len(df)} , ")

sys.stdout.write("\nQuestion that most people answer incorrectly: ")
for i in range(1,26):
	if len(df[df[i] == -1]) == max_question(df, -1):
		sys.stdout.write(f"{i} - {max_question(df, -1)} - {max_question(df, -1) / len(df)} , ")

#Tạo file txt từ data frame lưu điểm của học sinh
df["Grade"].to_csv(f"{text_file}_grades.txt", header = False)
