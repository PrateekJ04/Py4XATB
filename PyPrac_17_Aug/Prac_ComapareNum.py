#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1= int(input("Enter a number for num1: "))
num2= int(input("Enter a number for num2: "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1==num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num2} is greater than {num1}")