file_path = input("Enter the file path: ")
line_count = 0

with open(file_path, 'r') as file:
    for line in file:
        line_count += 1

print("Number of lines in the file:", line_count)
