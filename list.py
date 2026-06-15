prog_lang = ["Python", "C++", "Go"]
prog_lang[0] = "Java"
print(prog_lang)
#List are mutable

#if u want to remove an element from the list use this keyword del
del prog_lang[2]
print(prog_lang)

#use in keyword to check whether an element exist or not
print('Python' in prog_lang)
