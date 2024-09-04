"""Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle."""


triangle_side1= int(input("Enter a value of side1 for triangle: "))
triangle_side2= int(input("Enter a value of side2 for triangle: "))
triangle_side3= int(input("Enter a value of side3 for triangle: "))

if triangle_side1==triangle_side2 and triangle_side2==triangle_side3 and triangle_side3==triangle_side1:
    print("The triangle is Equilateral triangle")
elif triangle_side1!=triangle_side2 and triangle_side2!=triangle_side3 and triangle_side1!=triangle_side3:
    print("The triangle is scalene triangle")
else:
    print("The triangle is isosceles triangle")
