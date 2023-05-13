def countMaximumFrequencyCharacter(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    maximum_frequency = max(char_frequency.values())
    maximum_frequency_characters = [char for char, frequency in char_frequency.items() if frequency == maximum_frequency]
    return maximum_frequency_characters

string = input("Enter a string: ")
maximum_frequency_characters = countMaximumFrequencyCharacter(string)
print("Maximum frequency characters:", maximum_frequency_characters)
