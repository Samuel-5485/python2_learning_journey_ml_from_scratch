#for loop
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
for categorie in categories:
    for food in foods:
        print(categories, food)
#while loop
secret_number = 4
guess = 0
while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! try again')
print('You got it!')
#break
developers = ['Sami', 'Abdi', 'Chala']
for developer in developers:
    if developer == 'Abdi':
        break
    print(developer)
#continue
developers = ['Sami', 'Abdi', 'Chala']
for developer in developers:
    if developer == 'Abdi':
        continue
    print(developer)

words = ['sky','apple','rhythm','fly']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel'{letter}")
            break
        print(f"'{word}' has no vowels")

for num in range(3):
    print(num)

for num in range(40, 0, -10):
    print(num)

numbers = list(range(2, 11, 2))
print(numbers) 

lang = ['spanish', 'English', 'Chinese']
index = 0

for lan in lang:
    print(f"index {index} and language {lan}")
    index += 1

#enumerate()
list(enumerate(lang))
print(lang)

langs = ['spanish', 'English', 'Russian']
for index, lang in enumerate(langs):
    print(f"index {index} and language {lang}")

#zip(): a built-in function that takes multiple collections (like lists) and 
# pairs their elements together based on their index positions
developers = ['Naomi', 'Dario', 'Jessics']
ids = [1,2,3]
my_zip = list(zip(developers, ids))
print(my_zip)

for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {ids}")
#The enumerate() and zip() functions are very powerful,
#  and when combined with loops, can make your code much more concise

#What Are List Comprehensions and What Are Some Useful Functions to Work With Lists?
even_num = []
for num in range(21):
    if num % 2 == 0:
        even_num.append(num)

print(even_num)
#new version of the above code
even_num = [num for num in range(21) if num % 2 == 0]
print(even_num)
#
numbers = [1,2,3,4,5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
for num in numbers:
    if num % 2 == 0:
        print(f"{num} Even ")
    else:
        print(f"{num} Odd")
print(num)

#filter():function is used to select elements from
#  an iterable that met a specific condition. 
words = ['tree', 'sky', 'mountain', 'river']
def is_long_word(word):
    return len(word) > 4
long_words = list(filter(is_long_word, words))
print(long_words)

#map()
celsius = [0,10,20,30,40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

numbers = [4, 5, 6, 8]
total = sum(numbers)
print(total)

#i can alos pass in an optional start argument which sets 
#the initial value for the summation.
numbers = [4,5,6,7,8]
total = sum(numbers, 10)
print(total)

#you can also choose to use the start arg as a keyword arg 
numbers = [4,5,6,7,8]
total = sum(numbers, start=10)
print(total)

