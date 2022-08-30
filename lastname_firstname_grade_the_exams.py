#Import library
import pandas as pd
import time

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



