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

#append()
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

#if u want to add list by following the previous list
even_numbers = [7, 8, 9]
numbers.append(even_numbers)
print(numbers)

#extend()
numbers = [1,2,3,4,5]
even_numbers = [6,7,8]
numbers.extend(even_numbers)
print(numbers)

#insert(): you have to specify the index 
numbers = [1,2,3]
numbers.insert(2, 4)
print(numbers)

#remove():
numbers.remove(1)
print(numbers)

numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50) #only the first occurence not all of them

print(numbers)

#pop(): remove the at specified index 
numbers = [1,2,3,4] 
numbers.pop(1)
print(numbers)

#clear(): when u need to empty the list
numbers.clear()
print(numbers)

#sort()
numbers = [43, 23,67, 22]
numbers.sort()
print(numbers)

#sorted(): incontrast to sort()
numbers = [43, 23,67, 22]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

#reverse()
numbers.reverse()
print(numbers)

#use indext method to find elements
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java')
print(programming_languages)