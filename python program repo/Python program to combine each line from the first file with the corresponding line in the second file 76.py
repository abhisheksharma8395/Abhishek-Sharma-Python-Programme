file1 = input("Enter the path of the first file: ")
file2 = input("Enter the path of the second file: ")
output_file = input("Enter the path of the output file: ")

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for line1, line2 in zip(lines1, lines2):
        combined_line = line1.strip() + " " + line2.strip() + "\n"
        output.write(combined_line)

print("Files combined successfully.")
