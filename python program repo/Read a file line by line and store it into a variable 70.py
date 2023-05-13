file_path = input("Enter the file path: ")
file_contents = ""

with open(file_path, 'r') as file:
    for line in file:
        file_contents += line

print("File Contents:")
print(file_contents)
