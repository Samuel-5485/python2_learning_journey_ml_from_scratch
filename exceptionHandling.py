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
"""
