def replaceSubstring(string, old_substring, new_substring):
    new_string = string.replace(old_substring, new_substring)
    return new_string

string = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")
result = replaceSubstring(string, old_substring, new_substring)
print("String after replacing substring:", result)