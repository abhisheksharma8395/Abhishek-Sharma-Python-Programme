def isDictionaryEmpty(dictionary):
    return len(dictionary) == 0

my_dict = {}
if isDictionaryEmpty(my_dict):
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")