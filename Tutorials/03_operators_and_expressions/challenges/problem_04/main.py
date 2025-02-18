### Find root of the quadratic equations
import math

a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))

r1 = round(((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a)), 2)
r2 = round(((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a)), 2)

print(f"roots of the above equation is: x = ({r1}, {r2})")