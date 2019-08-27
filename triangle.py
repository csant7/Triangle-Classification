#Triangle Classification by Connor Santiago

def classifyTriangle(a, b, c):
    if a == b and b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or c == a:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

def rightTriangle(a,b,c):
    if (a*a) + (b*b) == (c*c):
        return "Right Triangle"
    else:
        return "Not a right triangle"

#Main Program:
print("\nPlease enter the 3 side lengths of your triangle. Make sure to enter the hypotenuse last.")
a = int(input("Side 1: "))
b = int(input("Sdie 2: "))
c = int(input("Side 3: "))

print(classifyTriangle(a, b, c))
print(rightTriangle(a, b, c))