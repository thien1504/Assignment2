#Import library
import pandas as pd
import time

'''Có 3 trường hợp line sẽ invalid
	TH1: ID của học sinh sai (len(ID) không bằng 9)
	TH2: Học sinh không trả lời được hết tất cả các câu
	TH3: Học sinh trả lời dư câu hỏi 
=> Tạo ra 3 list để lưu lại các trường hợp này
'''
list_invalid_id = []
list_invalid_grade = []
list_invalid_answer = []

# Hàm lọc ra các học sinh có mã học sinh sai (Input là text file, output là 1 list)
def invalid_ID (text_file):
	list_invalid_id = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if len(line.split(",")[0]) != 9:
				list_invalid_id.append(line)
	return list_invalid_id

# Hàm lọc ra các học sinh có dư câu trả lời
def invalid_answer(text_file):
	list_invalid_answer = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if len(line.split(",")) > 26:
				list_invalid_answer.append(line)
	return list_invalid_answer

# Hàm lọc ra các học sinh không trả lời được hết tất cả các câu
def invalid_grade(text_file):
	list_invalid_grade = []
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			l = line.split(",")
			for i in l:
				if i == "":
					list_invalid_grade.append(line)
					break
	return list_invalid_grade

# Hàm tính tổng dòng trong text file
def count_total_line(text_file):
	count = 0
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			count +=1
	return count


text_file = input("Enter a filename: ")

try:
	with open(f"{text_file}.txt") as fh:
		print(f"Successfully opened {text_file}.txt")
except:
	raise ("File cannot be found.")	

list_invalid_id = invalid_ID(text_file)
list_invalid_grade = invalid_grade(text_file)
list_invalid_answer = invalid_answer(text_file)

# Xóa các học sinh có ID sai và trả dư câu hỏi trong list học sinh không trả lời được hết tất cả các câu
# Vì xảy ra trùng lặp dữ liệu
for index, item in enumerate(list_invalid_grade):
	if item in list_invalid_id or item in list_invalid_answer:
		list_invalid_grade.pop(index)

# Valid line sẽ bằng tổng số dòng trong file trừ đi tổng số phần tử của 3 list bị invalid
valid_line = count_total_line(text_file) - len(list_invalid_id) - len(list_invalid_grade) - len(list_invalid_answer)\
# Số dòng invalid bằng tổng số phần từ của 3 list invalid
invalid_line = len(list_invalid_id) + len(list_invalid_grade) + len(list_invalid_answer)

print("**** ANALYZING ****\n")
time.sleep(1)
if invalid_line == 0:
	print("No errors found!")
	print("**** REPORT ****")
	print(f"Total valid lines of data: {valid_line}")
	print("Total invalid lines of data: 0 ")
else:
	with open(f"{text_file}.txt") as fh:
		for line in fh:
			if line in list_invalid_id:
				print("Invalid line of data: N# is invalid")
				print(line)
			elif line in list_invalid_grade or line in list_invalid_answer:
				print("Invalid line of data: does not contain exactly 26 values:")
				print(line)
	print("\n**** REPORT ****")
	print(f"Total valid lines of data: {valid_line}")
	print(f"Total invalid lines of data: {invalid_line}")

