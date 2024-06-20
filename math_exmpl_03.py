import math
def circumference(r):
    return math.tau * r

radius = float(input("Enter a number for radius: "))
print("Circumference = ", circumference(radius))
