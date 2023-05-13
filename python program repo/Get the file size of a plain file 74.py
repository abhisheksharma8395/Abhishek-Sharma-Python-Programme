import os

file_path = input("Enter the file path: ")

if os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)
    print("File size:", file_size, "bytes")
else:
    print("File does not exist or is not a plain file.")
