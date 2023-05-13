file_path = input("Enter the file path: ")

with open(file_path, 'r') as file:
    lines = file.readlines()

print("Lines in the file:")
for line in lines:
    print(line.rstrip())