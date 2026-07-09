try:
    y = 4/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division successful, result is: ", y)
finally:
    print("Execution completed.")
"""try: The block of code where you anticipate an error might occur.
    except: This block runs if an error of the specified type is raised inside the try block.
    In this case, dividing by zero raises a ZeroDivisionError, which is then caught and handled.

    else: Runs if no exception is raised in the try block.
    finally: Runs no matter what, whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources. 
"""

"""By using separate except clauses, you can make your error responses more specific and useful. """
try:
    num = int('0')
    result = 10 / num
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")

''' We can also use aliases to refer to the exception object which can provide more information...'''
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')

'''We can also catch multiple exceptions in a single except clause by specifying the exceptions as a tuple:'''
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')

'''Raise Statement: The raise statement allows you to trigger an exception manually. 
This can be usefull for validating input or enforcing certain conditions in your code. '''
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try: 
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

'''The raise statement can also be used to re-raise the current exception, which is particularly useful in exception handling'''
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')


def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')