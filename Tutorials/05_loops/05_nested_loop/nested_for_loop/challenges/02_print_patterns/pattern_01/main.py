"""
print the following pattern using python script

*
* *
* * *
* * * *
* * * * *

"""

for i in range(0, 5):
    for j in range(0, 5):
        if i >= j:
            print("*", end=" ")
    print()
