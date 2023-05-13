def countLeastFrequentCharacter(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    least_frequent_char = min(char_frequency, key=char_frequency.get)
    return least_frequent_char

string = input("Enter a string: ")
least_frequent_character = countLeastFrequentCharacter(string)
print("Least frequent character:", least_frequent_character)