def countWordFrequency(string):
    words = string.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

string = input("Enter a string: ")
frequency = countWordFrequency(string)
print("Word frequencies:", frequency)