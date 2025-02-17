### converting kms to miles
"""
km = float(input("Enter the kilometer(km.) here: "))
mile = km * 0.621371192
print(f"{km} kms. is equivalent to {round(mile, 2)} miles.")
"""

### Calculate area of a circle
import math

radius = float(input("Enter the value of the radius (in cm.): "))
# PI = 3.1415
# area = PI * radius ** 2
area = math.pi * radius ** 2
print(f"The area of the circle is: {round(area, 2)} sq. cm.")