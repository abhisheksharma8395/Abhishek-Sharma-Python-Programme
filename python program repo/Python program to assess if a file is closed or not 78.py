file_path = input("Enter the path of the file: ")

try:
    file = open(file_path, 'r')
    is_closed = file.closed
    file.close()
except FileNotFoundError:
    print("File not found.")
    exit()

print("Is the file closed?", is_closed)
