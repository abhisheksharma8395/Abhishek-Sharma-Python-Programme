import math

def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))

area, circumference = circle_properties(radius)
print("Area:", area)
print("Circumference:", circumference)
