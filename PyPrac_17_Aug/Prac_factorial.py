""" Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24"""

n= int(input("Enter a number for factorial: "))

if n==0:
    print("Factorial of given number is : 1")
elif n==1:
    print("Factorial of given number is : 1")
elif n>=2:
    for i in range(1,n):
        n = n*i
        i-=i
    print (f"The factorial of number is: {n}")
else:
    print("You have provided invalid input")

