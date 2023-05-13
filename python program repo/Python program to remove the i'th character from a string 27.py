def removeCharacter(string, i):
    if i < 0 or i >= len(string):
        return "Invalid index."
    else:
        new_string = string[:i] + string[i+1:]
        return new_string

string = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))
result = removeCharacter(string, i)
print("String after removing the character:", result)