#create a program that provides results for two numbers from user input
import math
num1= int(input("Enter a number for num1: "))
num2= int(input("Enter a number for num2: "))

max_funct= max(num1,num2)
sum_funct= num1+num2
sub_funct= num1-num2
mul_funct= num1*num2
div_funct= num1/num2
pow_funct= pow(num1,num2)

print("Below are the values of the numbers after command execution\n"f"Max value is: {max_funct}\n"f"Sum is :{sum_funct}\n"f"Subtraction  is: {sub_funct}\n"f"Multiplication is:{mul_funct}\n"
      f"Division is : {div_funct}\n"f"Power of num1 to num2 is: {pow_funct}")