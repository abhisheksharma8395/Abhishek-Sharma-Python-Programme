def multiplyDictionaryItems(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

my_dict = {'a': 2, 'b': 3, 'c': 4}
result = multiplyDictionaryItems(my_dict)
print("Multiplication of dictionary items:", result)