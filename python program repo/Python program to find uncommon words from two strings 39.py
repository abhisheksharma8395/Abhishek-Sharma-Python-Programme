def findUncommonWords(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    uncommon_words = words1.symmetric_difference(words2)
    return uncommon_words

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
uncommon_words = findUncommonWords(string1, string2)
print("Uncommon words:", uncommon_words)