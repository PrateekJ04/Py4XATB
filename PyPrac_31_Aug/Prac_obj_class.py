# Class and Object Assignment

class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def employee_function(self):
        print(f"Name of the Employee is: {self.name}")
        print(f"Age of the Employee is: {self.age}")
        print(f"Phone Number of the Employee is: {self.phone}")
        print(f"Address of the Employee is: {self.address}")
        print(f"Employee id of the Employee is: {self.eid}\n")

    def walk(self):
        print(self.name, "Can walk\n")

    def talk(self):
        print(self.name, "Can talk\n")

    def breathe(self):
        print(self.name, "Can Breathe\n")


Name = input("Enter Employee1 Name: ")
Age = int(input("Enter Employee1 Age: "))
PhoneNo = int(input("Enter Employee1 Phone no.: "))
Address = input("Enter Employee1 Address: ")
EID = int(input("Enter Employee1 EID: "))

print("\n================================================================\n")

Name2 = input("Enter Employee2 Name: ")
Age2 = int(input("Enter Employee2 Age: "))
PhoneNo2 = int(input("Enter Employee2 Phone no.: "))
Address2 = input("Enter Employee2 Address: ")
EID2 = int(input("Enter Employee2 EID: "))

E1_details = Employee(Name, Age, PhoneNo, Address, EID)
print("--------------------------------------------------------------")

E1_details.employee_function()
E1_details.walk()
E1_details.talk()
E1_details.breathe()

E2_details = Employee(Name2, Age2, PhoneNo2, Address2, EID2)
print("--------------------------------------------------------------")

E2_details.employee_function()
E2_details.walk()
E2_details.talk()
E2_details.breathe()
