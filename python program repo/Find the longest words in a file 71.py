file_path = input("Enter the file path: ")

with open(file_path, 'r') as file:
    words = file.read().split()

longest_words = []
max_length = max(len(word) for word in words)

for word in words:
    if len(word) == max_length:
        longest_words.append(word)

print("Longest words in the file:")
print(longest_words)
