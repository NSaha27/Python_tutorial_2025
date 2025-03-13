# Print n terms of fabonacci series (in this series, a value is the result of the summation of its previous two values)

print("Fabonacci series of n terms:")
term = int(input("Enter the term: "))
if term < 0:
    term = int(input("Enter a valid term: "))

prev_1 = int(input("Enter the first initial value: "))
prev_2 = int(input("Enter the second initial value: "))
cur_num = None
fabonacci = ""

for i in range(term + 1):
    fabonacci += str(prev_1) + ", "
    cur_num = prev_1 + prev_2
    prev_1 = prev_2
    prev_2 = cur_num

# fabonacci = str(prev_1) + ", "
# counter = 0
# while counter < term - 1:
#     fabonacci += str(prev_2) + ", "
#     cur_num = prev_1 + prev_2
#     prev_1 = prev_2
#     prev_2 = cur_num
#     counter += 1

print(f"The fabonacci series for {term}th terms is : {fabonacci}")
