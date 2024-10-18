# Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13
a = 0
b = 1
x = int(input("Enter a number: "))
fibo_series = [0]
if x == 1:
    print(a)
    print(b)
if x >= 1:
    for i in range(2, x + 1):
        num = a + b
        a = b
        b = num
        fibo_series.append(num)
    print("The fibonacci series for given no is: \n"f"{fibo_series}")
