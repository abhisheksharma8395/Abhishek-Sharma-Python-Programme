file_path = input("Enter the file path: ")
word_count = {}

with open(file_path, 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(word, ":", count)
