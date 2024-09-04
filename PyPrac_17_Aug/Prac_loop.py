"""Write a program that prints numbers from 1 to 100. # Loop For

However, for multiples of 3, print "Fizz" instead of the number, and

for multiples of 5, print "Buzz."

For numbers that are multiples of both 3 and 5, print "FizzBuzz."""

#You must enter a number n+1, in case you want to enter 100 enter 101
num = int(input("Enter a num: "))

for i in range(1,num):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%5==0 and i%3==0:
        print("FizzBuzz")
    else:
        print(f"{i}")
