file_path = input("Enter the file path: ")
n = int(input("Enter the number of lines to read: "))

with open(file_path, 'r') as file:
    lines = file.readlines()[-n:]

print("Last", n, "lines of the file:")
for line in lines:
    print(line.rstrip())