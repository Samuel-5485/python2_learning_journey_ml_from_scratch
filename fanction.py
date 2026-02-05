# Python Functions
# A function can return data as a result

def my_func():
    print("Hello this's a functions")
my_func()  #calling the functions
my_func()  #calling the functions 
my_func()  #calling the functions

def fahrenheit_to_celsius(fahreneit):
    return (fahreneit - 32) * 5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(55))

# Return Values
# function can send data back to the code that called them using the return statements
def get_greeting():
    return "hello from a function"
message = get_greeting()
# get_greeting()  nothing return why
# print(get_greeting()) correct
print(message)
# If a function doesn't have a return statement, it returns None by default.
