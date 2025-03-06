# effect of "else suit" with break statement
# if the loop is terminated with break statement before its condition becomes False, then, else suit will not work.

counter = 1
while counter <= 10:
    if counter > 5:
        break
    print(f"this is step number {counter}")
    counter += 1
else:
    print("this statement will be executed if the condition in while loop becomes False")

print("end of the program!")
