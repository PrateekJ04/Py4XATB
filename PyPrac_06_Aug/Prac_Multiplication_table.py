# Home Can you create a Program I will give you number(userinput and print table)
#Create a table of integer
def table_of_a_number(t):
    print(f"Multiplication Table for {t} is : ")
    for i in range (1,11):
        print(f"{t} x {i} = {t * i}")

table_of_a_number(5)