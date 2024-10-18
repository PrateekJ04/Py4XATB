#Define static method and static variables

a=10

class TestClass:

    @staticmethod
    def just_test():

        print("This is my static variable test")


print(a)
TestClass.just_test()