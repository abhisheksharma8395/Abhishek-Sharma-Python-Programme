file_path = input("Enter the path of the file: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        vowels = "aeiouAEIOU"
        vowel_count = 0

        for char in content:
            if char in vowels:
                vowel_count += 1

        print("Number of vowels in the file:", vowel_count)
except FileNotFoundError:
    print("File not found.")
