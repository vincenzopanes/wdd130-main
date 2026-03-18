length = float(input("What is the length of the rectangle? "))

while length < 0:
    print("Sorry. The length cannot be negative")
    length = float(input("What is the length of the rectangle? "))

width = float(input("What is the width of the rectangle? "))

while width < 0:
    print("Sorry. The width cannot be negative")
    width = float(input("What is the width of the rectangle? "))

area = length * width

print(f"The area is {area}")