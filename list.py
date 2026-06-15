prog_lang = ["Python", "C++", "Go"]
prog_lang[0] = "Java"
print(prog_lang)
#List are mutable

#if u want to remove an element from the list use this keyword del
del prog_lang[2]
print(prog_lang)

#use in keyword to check whether an element exist or not
print('Python' in prog_lang)

#list nested inside list
developer = ['Alice', 34, ['Rust', 'Python', 'C++']]
print(developer[2])
print(developer[2][1])

#Unpacking values from a list method to assign value to variable
developer = ['Jon', 12, 'Java developer']
name, age, job = developer
print(name)
print(age)
print(job)

#If u need to collect any remaining elements from a list use asterist*
name, *rest = developer
print(name)
print(rest)

#Slicing we use operator :
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']

#If u wann extract even num
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]