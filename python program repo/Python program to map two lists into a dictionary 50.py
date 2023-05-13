def mapListsToDictionary(keys, values):
    return dict(zip(keys, values))

keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
result = mapListsToDictionary(keys, values)
print("Mapped dictionary:", result)
