# #Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.

year = int(input("Enter a year: "))
if year%4==0:
    print(f"{year}: It's a leap year")
elif year%400==0 and year%100!=0 :
    print(f"{year}: It's a leap year")

else:
    print(f"{year}: It is not a leap year")