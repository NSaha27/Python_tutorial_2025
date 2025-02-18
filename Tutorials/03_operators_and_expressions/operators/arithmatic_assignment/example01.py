"""
+= - addition-assignment operator
-= - subtraction-assignment operator
*= - multiplication-assignment operator
**= - exponent-assignment operator
/= - float division-assignment operator
//= - floor division-assignment operator
%= - modulus-assignment operator

"""

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print(f"value of a was {a}")
a += 1
print(f"new value of a after addition is {a}")

print()

print(f"value of b was {b}")
b *= 2
print(f"new value of b after multiplication is {b}")

print()

a **= 3
print(f"new value of a after exponent is {a}")

print()

b /= 2
print(f"new value of b after float division is {b}")

print()

a //= 2
print(f"new value of a after floor division is {a}")

print()

b %= 3
print(f"new value of b after modulo-division is {b}")