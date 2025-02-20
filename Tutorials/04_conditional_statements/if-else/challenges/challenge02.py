# check for age eligibility for casting a vote

age = int(input("Enter your age: "))

if age >= 18:
    print("you're eligible for vote!")
else:
    print(
        f"sorry, you have to wait for another {18 - age} years to eligible for voting.")
