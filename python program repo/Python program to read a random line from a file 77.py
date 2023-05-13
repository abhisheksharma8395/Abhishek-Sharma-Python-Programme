import random

file_path = input("Enter the path of the file: ")

with open(file_path, 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)

print("Random line from the file:")
print(random_line)
