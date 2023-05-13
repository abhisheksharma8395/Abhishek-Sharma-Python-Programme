char = input("Enter a character: ")

if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")