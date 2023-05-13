def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area, perimeter = rectangle_properties(length, width)
print("Area:", area)
print("Perimeter:", perimeter)
