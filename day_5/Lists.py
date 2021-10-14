# Day 5: 30 Days of python programming

# Creating the list
# syntax


from ast import AugStore


lst = list()

empty_list = list() # this is an empty list, no item in the list
print(len(empty_list))  # 0

# syntax
lst = []

empty_list = [] # this is an empty list, no item in the list
print(len(empty_list))  # 0
fruits = ['banana', 'orange', 'mango', 'lemon']                 # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'] # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yogurth']         # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']   # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal products: ', animal_products)
print('Number of animal products: ', len(animal_products))
print('Web technologies: ', web_techs)
print('Number of web technologies: ', len(web_techs))
print('Countries: ', countries)
print('Number of countries: ', len(countries))

first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit)       # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing lists using negative indexing

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_fruit)     # mango

# Unpacking list items

lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)       # item1
print(second_item)      # item2
print(third_item)       # item3
print(rest)             # ['item4', 'item5']


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)      # banana
print(second_fruit)     # orange
print(third_fruit)      # mango
print(rest)             # ['lemon', 'lime', 'apple']
# Second Example
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)            # 1
print(second)           # 2
print(third)            # 3
print(rest)             # [4,5,6,7,8,9]
print(tenth)            # 10
# Third Example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]    # it results all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:]     # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]    # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index, ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end, ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1]   # a negative step will take the list in reverse order, ['lemon', 'mango', 'orange', 'banana']

# Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)       # ['avocado', 'apple', 'mango', 'lime']

# Checking Items in a List

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)   # True
does_exist = 'lime' in fruits
print(does_exist)   # False

# Adding items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)       # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)       # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# Inserting items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')   # insert apple between orange and mango
print(fruits)               # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')
print(fruits)               # ['banana', 'orange', 'apple', 'lime', 'mango', lemon']

# Removing Items From a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# Removing Items Using Pop

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# Removing Items Using Del

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)           # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)           # ['orange', 'lemon', 'kiwi', 'lime']
del fruits [1:3]        # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)           # ['orange', 'lime']
del fruits

# Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)           # []

# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)          # ['banana', 'orange', 'mango', 'lemon']

# Joining Lists
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato','Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)    # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)    # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers: ', negative_numbers) # Inetegers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits=['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables: ', fruits)

# Counting items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# Finding index of an item

print(fruits.index('orange'))
print(ages.index(24))           # 2, the first occurence

# reversing a list

fruits.reverse()
print(fruits)
fruits.reverse()
ages.reverse()
print(ages)
ages.reverse()

# Sorting List items

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

# sorted(): returns the ordered list without modifying the original list
print(sorted(fruits))
fruits = sorted(fruits, reverse=True)
print(fruits)

# Exercises: level 1
# 1.
empty_list = []

# 2.
list_with_more_than_five_items = [1,2,3,4,5,6,7]

# 3.
print(len(list_with_more_than_five_items))

# 4.
print(list_with_more_than_five_items[0])
print(list_with_more_than_five_items[int(len(list_with_more_than_five_items)/2)])
print(list_with_more_than_five_items[-1])

# 5.
mixed_data_types = ['Jacek', 28, 178, 'single', '2a Holyoake road']

# 6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.
print(it_companies)

# 8.
print(len(it_companies))

# 9.
print(it_companies[0], it_companies[int(len(it_companies)/2)],it_companies[-1])

# 10.
it_companies[0] = 'Twitter'
print(it_companies)

# 11.
it_companies.append('Lenovo')
print(it_companies)

# 12.
it_companies.insert(3, 'HP')

# 13.
it_companies[2]=it_companies[2].upper()

print(it_companies)

# 14.
companies = '#; '.join(it_companies)
print(companies)

# 15.
does_exist = 'Microsoft' in it_companies
print(does_exist)

# 16.
it_companies.sort()
print(it_companies)

# 17.
it_companies.reverse()
print(it_companies)

# 18.
new_it = it_companies[3:]
print(new_it)

# 19. 
new_it = it_companies[:-3]
print(new_it)

# 20.
new_it = it_companies[0:int(len(it_companies)/2)] + it_companies[int(len(it_companies)/2)+1:]
print(new_it)

# 21. 22. 23.

it_companies.pop(0)
it_companies.pop(-1)
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
full_stack=front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercise: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(ages[-1])
ages.append(ages[0])
ages.sort()
print(ages)
median = ages[int(len(ages)/2)]
average = sum(ages)/len(ages)
print(median)
print(average)
range_ages = min(ages) + max(ages)
print(abs(min(ages) - average) > abs(max(ages) - average))
