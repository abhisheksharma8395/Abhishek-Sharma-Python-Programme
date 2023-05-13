import reversed

# Function to reverse a string
def reverse_string(input_string):
    return ''.join(reversed.reverse(input_string))

# Get user input
user_input = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(user_input)

# Print the reversed string
print("Reversed string:", reversed_string)
