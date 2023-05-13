file_path = input("Enter the file path: ")
text = input("Enter the text to append: ")

with open(file_path, 'a') as file:
    file.write(text)

with open(file_path, 'r') as file:
    file_contents = file.read()

print("Updated File Contents:")
print(file_contents)
