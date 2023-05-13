def splitAndJoinString(string):
    words = string.split()
    joined_string = '-'.join(words)
    return joined_string

string = input("Enter a string: ")
joined_string = splitAndJoinString(string)
print("Joined string:", joined_string)