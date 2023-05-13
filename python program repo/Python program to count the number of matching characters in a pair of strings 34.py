def countMatchingCharacters(string1, string2):
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            count += 1
    return count

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
matching_characters = countMatchingCharacters(string1, string2)
print("Number of matching characters:", matching_characters)