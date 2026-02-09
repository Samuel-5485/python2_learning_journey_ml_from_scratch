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

#Positional Arguments: In this order matter when you call...
def my_func(animal, name):
    print("I have a", animal)
    print("My", animal)
my_func("buddy", "dog") #order matter

#mixing positional and keyword arguments
def my_func(animal, name, age):
    print("I've a", age, "year old", animal, "named", name)
my_func("dog", name = "Buddy", age = 6) #mixing positional and keyword arguments 

# Passing different data types
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function(["apple", "banana", "cherry"]) #passing a list as an argument

# Sending a dictionary as an argument
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_function({"name": "Alice", "age": 20}) #passing a dictionary as an argument

# return values
def my_function(x, y):
    return x + y
result = my_function(7, 4)
print(result)

# Returning different data types
def my_function():
    return [1, 2, 3, 4, 5]
num = my_function()
print(num)
print(num[0])
print(num[1])
print(num[2])
print(num[-1])

# positional only arguments
# you can specify that a function can have only positional arg
#to specify a positional-only argument, add, / after the arguments
def my_function(name, /):
    print("Hello", name)
# my_function(name = "Alice") # TypeError: my_function() got some positional-only arguments but keyword was given
my_function("Alice") #correct

# Keyword-only arguments
# To specify that can have only keyword argument, add * , before arguments
def my_func(*, name):
    print("Hello", name)
# my_func("Bro") # TypeError: my_func() take 0 positional arguments bu 1 was given
my_func(name = "Bro") #correct
# What is d/t between positional-only and keyword-only arguments?
# Positional-only arguments must be passed in the correct order and cannot be specifyed using their names when calling the function,
# while keyword-only arguments must be specifyed using their names when calling the function and cannot be passed positionally

# Combining positional-only and keyword-only
# you can combine both arg types in the same function
# Arguments before / are positional -only, and arguments after * are keyword-only
def my_calc(a, b, /, *, c, d):
    return a + b + c + d
result = my_calc(3, 4, c = 2, d = 9)
print(result)

# Python *args and **kwargs
# *args allows you to pass a variable number of non-keyword arguments to a function,
# while **kwargs allows you to pass a variable number of keyword arguments to a function.
def my_func(*args):
    for arg in args:
        print(arg)
my_func(1, 4, 5) #passing a variable number of non-keyword arguments
# Using *args to accept any number of positional arguments:
def my_func(*kids):
    print("The youngest child is " + kids[0])
    print("All arguments: ", kids)
    print("Type: ", type(kids))
# lists = my_func["Emil", "Tobias", "Linus"] TypeError: 'function' object is not subscriptable
my_func("Emil", "Tobias", "Linus")

# Using *args with a regular argument:
def my_func(greeting, *names):
    for name in names:
        print(greeting, name)
my_func("Hello", "Alice", "Bob")

# A function thata calculates the sum of any number of values:
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_all(4, 9, -3))
print(sum_all(3, 8, 2))
print(sum_all(3))

# finding the maximum value 
def max_value(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(max_value(7, 8, 2))

# Arbitrary keyword Arguments with **kwargs
# if you don't know how many keyword arguments will be passed to your function, 
# add two asterisks ** before the parameter name in the function definition
# why we use **kwargs? because it allows us to handle a variable number of
#  keyword arguments, which can be useful when we want to create flexible
#  function that can accept different types of input without having to define a fixed number of parameters

def my_func(**kwargs):
    print("Type", type(kwargs))
    print("Name: ", kwargs["name"])
    print("Age: ", kwargs["age"])
    print("All data: ", kwargs)
my_func(name = "Alice", age = 21, city = "New York", country = "USA",)

# Combining *args and **kwargs
# what is d/t between *args and **kwargs?
# *args is used to pass a variable number of non-keyword arguments to a function, 
# while **kwargs is used to pass a variable number of keyword arguments to a function 
# 
def my_func(title, *args, **kwargs):
    print("Title: ", title)
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)
my_func("My function", name = "Alice", age = 20, city = "New York")

def student_info(student_id, *courses, **details):
    print("Student ID: ", student_id)
    print("Courses: ", courses)
    print("Details: ", details)
student_info(101, "Math", "Cs", "IT", name = "Bob", age = 20, city = "AA")
# OR 
"""student_info(
    102,
    "Math",
    "Cs",
    "IT", 
    name = "Bob",
    age = 20,
    city = "AA"
)
"""
# Unpacking Arguments
# you can also use * and ** to unpack arguments when calling a function
def my_func(a, b, c):
    return a + b + c
numbers = (3, 8, 9) #  a tuple or you can use a list []
print(my_func(*numbers)) # unpacking a list as arguments

# unpacking a dictionary with **
def my_func(fname, lname):
    print("Hello", fname, lname)
person = {"fname": "John", "lname": "Doe"}
my_func(**person) # unpacking a dictionary as arguments

# Python Scope
# Scope refers to the region of a program where a variable is defined and can be accessed.
# In python, there are four types of scope: local, enclosing, global, and built-in.
# 1. Local Scope: A variable defined inside a function is in the local scope of that function and can only be accessed within that function.
def my_func():
    x = 8 # x is a local variable
    print(x)
my_func()

# 2. Global Scope: A variable defined outside of any function is in the global scope and can be accessed from anywhere in the code.
y = 10 # y is a global variable
def my_func():
    print(y) # accessing global variable inside a function
my_func()
print(y) # accessing global variable outside a function

# global keyword: is used to declare that a variable inside a function is global(it belongs to the global scope).
# it allow you to modify a global variable inside a function
def my_func():
    global y # to modify the global variable
    y += 5
my_func()
print(y) # accessing global variable inside a function
# 3. Enclosing Scope: A variable defined in an enclosing function is in the enclosing scope and can be accessed by nested function.
#   nonlocal keyword: is used to work with variables inside functions,
#  it's belong to the outer function. it allows you to modify the outer function variable
def outer_func():
    z = 4 # z is in the enclosing scope
    def inner_func():
        nonlocal z # to modify the enclosing variable
        z += 1
        print(z) # accessing enclosing variable inside nested function
    inner_func()
outer_func()

# 4. Built-in scope: A variable defined in the built-in scope is a built-in function or constant that is always available in python.
print(len("Hello")) # len is a built-in function
print(max(3, 8, 2)) # max is a built-in function

# question 
#1 what will be the output of the following code?
x = 2
def my_func():
    x = 7
my_func()
print(x)
#2 what will be the output of the following code?
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)

# Python Decorators
# A decorator is a function that take another function as an argument
#  and extends the behavior of the latter function without explicitly modifying it.
# basic decorator: @decorator_name apply above the function
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def greet():
    return "hello from a function"
print(greet())

#Multiple decorators: you can apply multiple decorators to a function by stacking them on top of each other
def add_exclamation(func):
    def myinner():
        return func() + "!"
    return myinner
@add_exclamation
def my_func():
    return "hello from a function"

@add_exclamation
def other_func():
    return "welcome to python"
print(my_func())
print(other_func())

#Arguments in decorated functions: if the original function takes arguments, the inner function in the decorator 
#must also accept those arguments and pass them to the original function when calling it.
def repeat(func):
    def myinner(y):
        return func(y).upper()
    return myinner
@repeat
def my_func(name):
    return f"hello, {name} how are you?"
print(my_func("Alice")) 

#secure the function with *args and **kwargs
def change_case(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner
@change_case
def greet(name):
    return "Hello " + name
print(greet("John"))

#Preserving function metadata: function in python has metadata that can be accessed using the __name__ and __doc__ attributes
def myfunc():
    return "have a great day!"
print(myfunc.__name__) # output: myfunc,cuz the function name is myfunc
print(myfunc.__doc__) # output: None, cuz we didn't add a docstring to the function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def my_func():
    """This is the original function"""
    return "Hello from a function"
print(my_func.__name__) # output: wrapper, cuz the function name is wrapper
print(my_func.__doc__) # output: This is the wrapper function, cuz the docstring

#import functools.wraps to preserve the original function name and docstring
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func()
    return wrapper
@my_decorator
def my_func():
    """This is the original function"""
    return "Hello from a function"
print(my_func.__name__) # output: my_func, cuz the function name is my_func

#question
#1. What will be the output of the following code?
def upper(f):
  def w():
    return f().upper()
  return w

def exclaim(f):
  def w():
    return f() + "!"
  return w

@upper
@exclaim
def say():
  return "hi"

print(say())