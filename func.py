"""What Are Lambda Functions and How Do They Work?"""
def square(num):
    return num ** 2
print(square(4))

numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

'''what the difference between map and filter'''
numbers = [1,2,3,4,5]
square = lambda x: x ** 2
squared_num = list(map(square, numbers))
print(squared_num)

numbers = [1,2,3]
def square(nums):
    return nums ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)
'''Another version'''
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)