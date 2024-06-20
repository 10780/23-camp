import math
def circle_area(r):
    return math.pi*r**2

radius = float(input("Enter a number for radius: "))
print("Circle area = ", circle_area(radius))
