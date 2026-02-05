# Python Global variables
#Global variables can be used by everyone, both inside of functions and outside.
#create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
#using global
x = "awesome"
def myfunc():
    global x
    x = "wow"
myfunc()
print("python is " + x)