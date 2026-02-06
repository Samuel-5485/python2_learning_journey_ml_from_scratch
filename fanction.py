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

# The pass statement
# function definition can't be empty. if you need to create a function
# placeholder without any code, use the pass statement
# If a function doesn't have a return statement, it returns None by default.
for z in [0,1,2]:
    pass

def myfunc():
    pass
# keep in mind:  when you code pass as a default think like of this 
# you forget to calculate 5*6+4-3 but at the time you remember,
#  how to solve it you will come back and solve
for i in range(1, 12):
    print(i)

# Python function arguments
# A function can have arguments, which are values you can pass to the function when you call it.
     #A function with one argument
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
  #or
def greet(fname):
    print(fname + " Ahmed")
greet("Ali")

# A function with multiple arguments
def add(a, b):
    return a + b
print(add(4, 8))

def my_function(fname, lname):
    return fname + " " + lname
    # return f"{fname} {lname}"
    # print(fname + " " + lname)
name = my_function("John", "Doe")
print(name)

# Parameter vs Argument
# A parameter is a variable in the function definition that represents a value that will be passed to the function when it is called.
# An argument is the actual value that is passed to the function when it is called.
def my_function(para1, para2):
    return para1 + para2
result = my_function(5, 9) # 5 and 9 are arguments
print(result)

# try to call a function with missing arguments
def multiply(x, y):
        return x * y
try:
    print(multiply(5))
except TypeError:
    print("TypeError: multiply() missing 1 required positional argument")

print(multiply(5, 8))
 # TypeError: multiply() missing 1 required positional argument:

# Default Parameter Values
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet()) #use default value
print(greet("Alice")) #override default value

# Keyword Arguments:In this order doesn't matter when you call... 
# you can send aarguments with the key = value syntax. this way the order of the arguments doesn't matter
def greet(name, age):
    return f"Hello, {name}! Are you {age} years old?"
print(greet(age=20, name="Alice")) #order doesn't matter
# print(greet(20, "Alice")) #But if we code like this b/c order matter