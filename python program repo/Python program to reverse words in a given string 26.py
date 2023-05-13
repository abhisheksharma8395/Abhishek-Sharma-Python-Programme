def reverseWords(string):
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

string = input("Enter a string: ")
reversed_string = reverseWords(string)
print("Reversed string:", reversed_string