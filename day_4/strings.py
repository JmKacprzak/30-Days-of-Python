# Day 4: 30 Days of python programming

# Challanges
letter = 'p'                    # A string could be a single character or a bunch of text
print(letter)                   # P
print(len(letter))              # 1
greeting = 'Hello, World!'      # String could be made using a single or double quote, "Hello, World!"

# Multiline strings
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why i created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Jacek'
last_name = 'Kacprzak'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Jacek Kacprzak
# Checking the length of a string using len() built-in function
print(len(first_name))  # 5
print(len(last_name))   # 8
print(len(first_name) > len(last_name)) # False
print(len(full_name))   # 14

# Escape Sequences in String
print('I hope everyone is enjoying the Python Challange. \nAre you?')   # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello,World!\"')  # To write a double quote inside a single quote

# String formatting
# Old style formatting
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string) # "The following are python libraries:['Fjango', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']"

# New Style String Formatting (str.format)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach{}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))   # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a** b))

# String Interpolation/ f-Strings
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Python strings as sequences of characters

# Unpacking characters
language = 'Python'
a,b,c,d,e,f = language  # unpacking squence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing Characters in Strings by Index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter)# y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing Python Strings
language = 'Python'
first_three = language[0:3] # Starts at zero index and up to 3 but not include 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)   # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW, olleH

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto)  #Pto

# String Methods
challenge = 'thirty days of python'
print(challenge.capitalize())   # 'Thirsty days of python

print(challenge.count('y'))     # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2

print(challenge.endswith('on'))     # True
print(challenge.endswith('tion'))   # False

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

print(challenge.rfind('y'))
print(challenge.rfind('th'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7


challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 8


challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  #True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False, space is not an alphanumeric character

challenge = 'thirty days of python'
print(challenge.isalpha())  # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())        # False

challenge = 'thirty days of python'
print(challenge.isdecimal())    # False
challenge = '123'
print(challenge.isdecimal())    # True
challenge = '\u00B2'
print(challenge.isdecimal())      # False
challenge = '12 3'
print(challenge.isdecimal())    # False, space not allowed

challenge = 'thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())  # True
challenge = '\u00b2'
print(challenge.isdigit())  # True

num = '10'
print(num.isnumeric())  # True
num = '\u00BD'  # 1/2
print(num.isnumeric())  # True
num = '10.5'
print(num.isnumeric())  # False

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

web_tech = ['HTML', 'Css', 'JavaSript', 'React']
result = ' '.join(web_tech)
print(result)   # 'HTML CSS JavaScript React'

result = '# '.join(web_tech)
print(result)

challenge = 'thirty days of python'
print(challenge.strip('noth'))  

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))

challenge = 'thirty days of python'
print(challenge.title())

challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = '30 days of python'
print(challenge.startswith('thirty'))

# Exercises - Day 4

# 1.
sentence = 'thirty ' + 'days ' + 'of ' + 'python '
print(sentence)

# 2. 3. 4. 5.

space = ' '
company = 'Coding' + space + 'For' + space + 'All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
sub_string = company[7:]
print(sub_string)

# 10.
print(company.find('Coding'))

# 11.
company=company.replace('Coding', 'Python')
print(company)

# 12.
print(company.replace('All', 'Everyone'))

# 13.
company = 'Coding For All'
print(company.split())

# 14.
pages = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(pages.split(','))

# 15.
print(company[0])

# 16.
print(len(company)-1)

# 17.
print(company[10])

# 20.
print(company.index('C'))

# 21.
print(company.index('F'))

# 22.
print(company.rfind('l'))

# 23.
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24.
print(sentence.rindex('because'))

# 25.
print(sentence.replace('because ',''))

# 28.
print(sentence.startswith('Coding'))

# 30.
sentence = '   Coding for all    '
print(sentence.strip(' '))

# 32.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

# 33.
print('I am enjoying this challenge.\nI just wonder what is next')

# 34.
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
radius = 10
area = 3.14 * radius ** 2
print('radius = {}'.format(radius))
print('area = 3.14 * radius ** 2')
print('The area of a cricle with radius {} is {} meters square'.format(radius, area))