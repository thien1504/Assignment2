file_open = input("Enter a filename: ")

try:
	with open(file_open) as fh:
		print("Successfully opened")
except:
	print("File cannot be found.")
