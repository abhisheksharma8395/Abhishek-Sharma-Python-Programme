def isSubstringPresent(string, substring):
    if substring in string:
        return True
    else:
        return False

string = input("Enter a string: ")
substring = input("Enter a substring to search: ")
if isSubstringPresent(string, substring):
    print("Substring is present in the string.")
else:
    print("Substring is not present in the string.")