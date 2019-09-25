# Triangle Classification by Connor Santiago


def classify_triangle(side_a, side_b, side_c):
    """classify"""
    if side_a == side_b and side_b == side_c:
        return "Equilateral Triangle"
    elif side_a == side_b or side_b == side_c or side_c == side_a:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


def right_triangle(side_a, side_b, side_c):
    """right"""
    if (side_a * side_a) + (side_b * side_b) == (side_c * side_c):
        return "Right Triangle"
    else:
        return "Not a right triangle"


# Main Program:
print("\nPlease enter the 3 side lengths of your triangle. Make sure to enter the hypotenuse last.")
INPUT_A = int(input("Side 1: "))
INPUT_B = int(input("Sdie 2: "))
INPUT_C = int(input("Side 3: "))

print(classify_triangle(INPUT_A, INPUT_B, INPUT_C))
print(right_triangle(INPUT_A, INPUT_B, INPUT_C))
