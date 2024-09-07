""""The wrapper function is used to call other function at which decorator is assigned"""

def outer_main_function(abc):
    def inner_wrapper_function():
        print("Before Execution")
        abc() #Function(extenal_function) will be called at this point and after function is executed next line will be executed
        print("After Execution")
    return inner_wrapper_function()


@outer_main_function
def external_function():
    print("i am getting executed")
