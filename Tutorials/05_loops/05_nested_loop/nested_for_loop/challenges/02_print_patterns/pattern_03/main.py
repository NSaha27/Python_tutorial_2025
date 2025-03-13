"""
print the following pattern -
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

# process 1
maxStars = 5
# upper part of the pattern
for i in range(0, maxStars):
    for j in range(0, i + 1):
        if j <= i:
            print("*", end=" ")
    print()

# lower part of the pattern
for i in range(0, maxStars - 1):
    for j in range(0, maxStars - 1):
        if j >= i:
            print("*", end=" ")
    print()
"""
# process 2
maxStars = 5
# upper part of the pattern
for i in range(1, maxStars + 1):
    print("* " * i)

# lower part of the pattern
for i in range(maxStars - 1, 0, -1):
    print("* " * i)
