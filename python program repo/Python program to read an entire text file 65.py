file_path = input("Enter the file path: ")

with open(file_path, 'r') as file:
    file_contents = file.read()

print("File Contents:")
print(file_contents)

