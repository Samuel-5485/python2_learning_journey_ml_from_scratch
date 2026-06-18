#What Are Some Common Techniques to Loop Over a Dictionary?
""".type(), .keyS(), and .items() """

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
#value
for price in products.values():
    print(price)
#key
for price in products.keys():
    print(price)
#same as key
for price in products:
    print(price)
#items
for price in products.items():
    print(price)

#print side by side
for product, price in products.items():
    print(product, price)

for product, price in products.items():
    products[product] = round(price * 0.9)
print(products)

#enumerate: assigns an integer to each key, we get tuple
for product in enumerate(products):
    print(product)

for index, product in enumerate(products):
    print(index, product)

for index, product in enumerate(products.items()):
    print(index, product)

for index, product in enumerate(products.items(), 1):
    print(index, product)

#What Are Sets, and How Do They Work?
""".remove() .discard() .disjoint()"""
my_set = {1,2,3,4,5}
your_Set = {2,4,5,6,7}
print(your_Set.issubset(my_set))
print(my_set.issuperset(your_Set))
print(my_set | your_Set) #union
print(my_set & your_Set) #intersection
print(my_set - your_Set) #difference
print(my_set ^ your_Set) #symetric difference
my_set -= your_Set
print(my_set)
print(7 in my_set)