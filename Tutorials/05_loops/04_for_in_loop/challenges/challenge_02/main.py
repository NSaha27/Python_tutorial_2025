# print n terms of AP series

print("AP series for given nth terms:")
term = int(input("Enter the term: "))
if term < 0:
    term = int(input("Enter a valid term: "))

diff = int(input("Enter the difference between two terms: "))

AP = ""
prev_term = 1
counter = 1
while counter <= term:
    AP += str(prev_term) + ", "
    prev_term += diff
    counter += 1

print(f"AP series for {term}th term is : {AP}")
