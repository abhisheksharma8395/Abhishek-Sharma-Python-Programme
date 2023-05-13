def rotateString(string, rotations):
    length = len(string)
    rotations = rotations % length
    rotated_string = string[rotations:] + string[:rotations]
    return rotated_string

string = input("Enter a string: ")
rotations = int(input("Enter the number of rotations: "))
result = rotateString(string, rotations)
print("Rotated string:", result)