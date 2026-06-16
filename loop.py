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