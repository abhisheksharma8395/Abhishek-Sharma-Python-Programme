def printEvenLengthWords(string):
    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

string = input("Enter a string: ")
print("Even length words in the string:")
printEvenLengthWords(string)