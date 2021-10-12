# Day 3: 30 Days of python programming

# Challanges
# Boolean Values
print(True)
print(False)

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)          # 3
print('Subtraction: ', 2 - 1)       # 1
print('Multiplication: ', 2 * 3)    # 6
print('Division: ', 4 / 2)          # 2.0 Division in Python gives floating number
print('Division: ', 6 / 2)          # 3.0
print('Division: ', 7 / 2)          # 3.5
print('Division without the remainder: ', 7 // 2)   # 3, gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 3)   # 2
print('Modulus: ', 3 % 2)           # 1, Gives the remainder
print('Exponentation: ', 2 ** 3)    # 8 it means 2 * 2 * 2

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a - b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                          # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

print(3 > 2)        # True, because 3 is greater than 2
print(3 >= 2)       # True, because 3 is greater than 2
print(3 < 2)        # False, because 3 is greater than 2
print(2 < 3)        # True, because 2 is less than 3
print(2 <= 3)       # True, because 2 is less than 3
print(3 == 2)       # False, because 3 is not equal to 2
print(3 != 2)       # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))   # False
print(len('mango') != len('avocado'))   # True
print(len('mango') < len('avocado'))    # True
print(len('milk') != len('meat'))       # False
print(len('milk') == len('meat'))       # True
print(len('tomato') == len('potato'))   # True
print(len('python') > len('dragon'))    # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)


print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)   # True - because both statements are true
print(3 > 2 or 4 < 3)   # True - because one of the statements is true
print(3 < 2 or 4 < 3)   # False - because both of the statements are false
print('True or False: ', True or False)
print(not 3 > 2)        # False - because 3>2 is true, then not True gives False
print(not True)         # False - Negation, the not operator turns true to false
print(not False)        # True
print(not not True)     # True
print(not not False)    # False

# Excercises = Day 3

# 1. Declare your age as integer value
my_age = 28

# 2. Declare your height as a float variable
my_height = 178.0

# 3. Declare a variable that store a complex number
complex_number = 1 + 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base = input('Enter base of the triangle: ')
height = input('Enter height of the triangle: ')
base=float(base)
height=float(height)
area_of_triangle = 0.5 * base * height
print('Area of the triangle is: ', area_of_triangle)

# 5. Write a script that prompts the user to enter side a, side b, side c of the triangle. Calculate the perimeter of the triangle
side_a = input('Enter side a of the triangle: ')
side_b = input('Enter side b of the triangle: ')
side_c = input('Enter side c of the triangle: ')
side_a=int(side_a)
side_b=int(side_b)
side_c=int(side_c)
perimeter_of_triangle = side_a + side_b + side_c
print('Perimeter of the triangle is: ', perimeter_of_triangle)

# 6. Get length and width of a rectangle using prompt. Calculate its area and perimeter
length = input('Enter length of rectangle: ')
width = input('Enter width of rectangle: ')
length=int(length)
width=int(width)
area_of_rectangle = length * width
perimeter_of_rectangle = 25 * (length + width)
print('Area of the rectangle is: ', area_of_rectangle)
print('Perimeter of the rectangle is: ', perimeter_of_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area and circumference where pi = 3.14
radius = input('Enter radius of a circle: ')
radius=float(radius)
area_of_circle = 3.14 * radius * radius
circumference_of_circle = 2 * 3.14 * radius
print('Area of the circle is: ', area_of_circle)
print('Circumference of the circle is: ', circumference_of_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2
y = 2 * 0 - 2
x = (0 + 2)/2
print('Slope is 2')
print('x-intercept is: ', x)
print('y-intercept is: ', y)

# 9. Find the slope and Euclidean distance between point (2, 2) and point (6, 10)
slope = (6 - 2)/(10 - 2)
euclidean_distance = (((6 - 2)**2)+((10-2)**2))**0.5
print('Slope: ', slope)
print('Euclidean distance: ', euclidean_distance)

# 10. Compare the slopes in tasks 8 and 9
print(slope > 2)
print(slope == 2)
print(slope < 2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
y = 0 ** 2 + 6 * 0 + 9
print('y for x = 0: ', y)
y = (-3) ** 2 + 6 * -3 + 9
print('y for x = -3: ', y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
lenght_python = len('python')
length_dragon = len('dragon')
print(lenght_python != length_dragon)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python?????????

# 16. Find the length of the text python and convert the value to float and convert it to string
lenght_python = len('python')
print(type(lenght_python))
lenght_python = float(lenght_python)
print(type(lenght_python))
lenght_python = str(lenght_python)
print(type(lenght_python))

# 17. Even numebers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
check_if_even = input('Enter an integer: ')
check_if_even = int(check_if_even)
print('Your number is even: ', (check_if_even % 2) == 0)

# 18. Check if the floor division of 7 by 3 is equal to the int converted balue of 2.7
print((7 // 3) == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter how many hours you work per week: ')
rate_per_hour = input('Enter your hourly rate: ')
hours = float(hours)
rate_per_hour = float(rate_per_hour)
print('Your weekly earning is: ', hours*rate_per_hour)

# 22. Write a script that prompts the user to enter number of years. Calculate number of seconds a person can live. Assume a person can live a hundred years
years_lived = input('Enter number of years you have lived: ')
years_lived=int(years_lived)
print('You have lived for ', years_lived * 31536000, ' seconds')

# 23. Write a Python script that displays the following table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')