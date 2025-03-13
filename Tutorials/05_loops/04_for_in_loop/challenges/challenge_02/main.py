# print n terms of AP series

print("AP series for given nth terms:")
term = int(input("Enter the term: "))
if term < 0:
    term = int(input("Enter a valid term: "))

init = int(input("Enter the initial value: "))
if init < 0:
    init = int(input("Enter a valid initial value: "))

diff = int(input("Enter the difference between two terms: "))
if diff < 0:
    diff = int(input("Enter a valid difference: "))

AP = ""
for n in range(init, term * diff + init, diff):
    AP += str(n) + ", "

print(f"AP series for {term}th term is : {AP}")
