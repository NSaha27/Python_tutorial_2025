# Find constants from a string

str1 = "Hello guys, Welcome to the world of python. We are luckey to have you here"

constants = ""
for ch in str1:
    if ch == "a" or ch == "A" or ch == "e" or ch == "E" or ch == "i" or ch == "I" or ch == "o" or ch == "O" or ch == "u" or ch == "U" or ch == " " or ch == "," or ch == ".":
        continue
    constants += ch + ", "

print(f"constants in the above string are : '{constants}'")
