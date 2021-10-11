# Day 2: 30 Days of python programming
import math

# Exercises: Level 1
first_name='Jacek'
last_name='Kacprzak'
full_name='Jacek Kacprzak'
country='Poland'
city='Warsaw'
age=28
year=2021
is_married=False
is_true=True
is_light_on=True
first_name_spouse, last_name_spouse, country_spouse, age_spouse='Jessica', 'Bedson', 'England', 23

# Exercises: Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(len(first_name))
compare=len(first_name)>len(last_name)
print(compare)
num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two
print('The Sum: ', total)
print('The Difference: ', diff)
print('The Multiplication: ', product)
print('The Division: ',division)
print('The Remainder: ', remainder)
print('The Exponent: ', exp)
print('The Floor division: ', floor_division)

radius=30
area_of_circle=radius**2*math.pi
circum_of_circle=radius*2*math.pi
area_of_circle=round(area_of_circle, 2)
circum_of_circle=round(circum_of_circle, 2)
print('Radius is: ', radius)
print('Area of circle is: ', area_of_circle)
print('Circumference of Circle is: ', circum_of_circle)

radius=input('Type radius of Circle to calculate area and circumference: ')
radius=float(radius)
area_of_circle=radius**2*math.pi
circum_of_circle=radius*2*math.pi
area_of_circle=round(area_of_circle, 2)
circum_of_circle=round(circum_of_circle, 2)
print('Radius is: ', radius)
print('Area of circle is: ', area_of_circle)
print('Circumference of Circle is: ', circum_of_circle)

first_name=input('What is your name: ')
last_name=input('What is your last name: ')
country=input('What country are you from: ')
age=input('How old are you: ')
print('Your name is: ', first_name,' ', last_name)
print('You are from ', country)
print('You are ', age, ' years old')

help('keywords')