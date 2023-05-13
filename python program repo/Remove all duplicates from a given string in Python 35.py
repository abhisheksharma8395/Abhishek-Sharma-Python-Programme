def removeDuplicates(string):
    return ''.join(set(string))

string = input("Enter a string: ")
result = removeDuplicates(string)
print("String after removing duplicates:", result)