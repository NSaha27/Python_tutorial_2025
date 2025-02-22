# check if a lowercase character is a valid consonant or not

userInput = input("Enter an alphabet: ").lower()

if userInput != "a" and userInput != "e" and userInput != "i" and userInput != "o" and userInput != "u":
    print(f"'{userInput}' is a valid consonant")
else:
    print(f"'{userInput}' is a vowel")
