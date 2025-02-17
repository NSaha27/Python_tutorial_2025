### Calculate area of a cuboid

length = float(input("Enter the length of the cuboid (in cm.): "))
breadth = float(input("Enter the breadth of the cuboid (in cm.): "))
height = float(input("Enter the height of the cuboid (in cm.): "))
area = 2 * (length*breadth + length*height + breadth*height)
print(f"The area of the cuboid is {area} sq. cm.")