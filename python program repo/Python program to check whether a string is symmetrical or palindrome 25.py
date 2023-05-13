def isSymmetricalString(string):
    return string == string[::-1]

string = input("Enter a string: ")
if isSymmetricalString(string):
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")