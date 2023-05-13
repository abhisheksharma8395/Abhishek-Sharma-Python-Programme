def snakeToPascal(string):
    words = string.split('_')
    pascal_case = ""
    for word in words:
        pascal_case += word.capitalize()
    return pascal_case

snake_case = input("Enter a snake case string: ")
pascal_case = snakeToPascal(snake_case)
print("Pascal case string:", pascal_case)