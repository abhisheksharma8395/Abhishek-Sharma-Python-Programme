def containsAllVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel not in string.lower():
            return False
    return True

string = input("Enter a string: ")
if containsAllVowels(string):
    print("String contains all vowels.")
else:
    print("String does not contain all vowels.")