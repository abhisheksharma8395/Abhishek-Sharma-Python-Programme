def replaceDuplicateOccurrences(string):
    char_frequency = {}
    new_string = ''
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
            new_string += '$'
        else:
            char_frequency[char] = 1
            new_string += char
    return new_string

string = input("Enter a string: ")
result = replaceDuplicateOccurrences(string)
print("String after replacing duplicate occurrences:", result)
