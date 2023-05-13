def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Enter your age: "))

if check_voting_eligibility(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")