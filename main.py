name = input('What is your name?')
print(int(3.14))

def hello():
    print('Hello World')
hello()

def calculate(a,b):
    print(a + b)
my_sum = calculate(4, 5)
print(my_sum)

#What is the default return value of a function in Python? None
#What is the term for a placeholder variable in a function? parameter
#What keyword is used to define a custom function in Python? def

#What Is Scope in Python and How Does It Work?
#In Python, scope determines the point at which you can access a variable. It's what controls the lifetime of a variable and how it is resolved in different parts of the code.

# To correctly determine scope, Python follows the LEGB rule, which stands for the following:

        # Local scope (L): Variables defined in functions or classes.

        # Enclosing scope (E): Variables defined in enclosing or nested functions.

        # Global scope (G): Variables defined at the top level of the module or file.

        # Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.
my_var = 13#globally scoped
def my_func():
    my_var = 12
    print(my_var) #locally scoped to my_func
my_func()
print(my_var) #NameError

#Enclosing scope:means that a function that's nested inside another function can 
# access the variables of the function it's nested within

def outer_func():
    msg = 'Hello there!' #localy scoped

    def inner_func(): #nested func
        print(msg)
    inner_func()
outer_func()

def outer_func():
    msg = 'Hi'
    res = "" #declare res in the enclosing scope

    def inner_func():
        nonlocal res #why we said here nonlocal: Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg) #accessing msg from outer_func
    inner_func()
outer_func()
#And if you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword:

my_var_1 = 5
def show_var():
    global my_var_2
    my_var_2 = 18
    print(my_var_1)
    print(my_var_2)
show_var()

#You can also use the global keyword to modify a global variable:
my_var = 123
def change_var():
    global my_var
    my_var = 120
change_var()
print(my_var)

#built-in scope refers to all of Python's built-in
#  functions, modules, and keywords, and are available anywhere in your program:
print(str(23))
print(type(4.23))
print(isinstance(3, str))

#Escaping Strings
msg = 'It\'s a sunny day'
print(msg)