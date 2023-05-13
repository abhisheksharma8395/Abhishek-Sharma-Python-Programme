def findDuplicateCharacters(string):
    duplicate_characters = []
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            duplicate_characters.append(char)
    return duplicate_characters

string = input("Enter a string: ")
result = findDuplicateCharacters(string)
print("Duplicate characters:", result)