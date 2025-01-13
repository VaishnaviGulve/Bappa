# VARIABLES
name = "vaishnavi" #string
age = 18
price = 82000
print(name)
print("my age is : ", age)

# Rules for Identifires :
# 1. only valid python identifiers , like uppercase , lowercase , digits or underscore.
# 2. can not start with digits .
# 3. we cant use special symbols like ,!,@,$,#,%..
# 4. can be of any length

print(type(name))
print(type(age))

# DATA TYPES
# Integers (=ve,-ve,0)
# String ("vaishnavi","karan")
# Float (3.11, 44.44)
# Boolean (True, False)
# None (a = none)

age = 18
old = False
a = None
print(type(old))
print(type(a))

# KEYWORDS
# Reserved words in python.
# python is case sensitive language.

# print sum 
a = 2
b = 5
c = a+b
print(c)
d = a-b
print(d)

# Comments in python
# 1. single line comment
# 2. multi line comment

print("hello world")
#print("hello world")

# Types of Operators
# symbol that performs a certain operation between operands.
# 1. Arithmetic Operators (+,-,*,/,%,**)
# 2. Relational/ Comparison Operators (==,!=,<,>,<=,>=)
# 3. Assignment Operators (=,+=,-=,*=,%=,**=)
# 4. Logical Operators (not,and,or)

# Arithmetic Operators 
a = 5 
b = 6
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b) #a^b

# Relational / compasion Operators 
# == to check equality
# != not equal to
# >= greater than equal to
# <= less than equal to

a = 50 
b = 40
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Assignment Operator
num = 10
num = num+10 #  or num+=10 ,-= , /= , *= 
print(num)

# logical Operators
# as like logic gates
print(not True)
print(not False)
print(not a<b)
val1 = True
val2 = False
print(val1 and val2)
print(val1 or val2)

# Type Conversion
a = 2 
b = 4.25
sum = a+b 
print(sum)

# Type Casting 
a = float("2")
b = 4.25
print(type(a))
print(a+b)

# Input in Python
# used to accept values from users 
# result of input is always a str
input(" enter your name: ")
name = input(" enter your name ")
print("welcome",name)
print(type(name))

# PRACTICE QUESTIONS

# Write a program to input 2 numbers & print their sum ?
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
sum = num1+num2
print("sum",sum)

# WAP to input side of square & print its area? 
side = 34
area = side*side
print("area=",area)

# WAP to input 2 floating point numbers & print their average ?
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
avg = (num1+num2)/2
print("average = ",avg)

# WAP to input 2 int numbers , a & b. print True if a is greater than or equal to b. if not print False. 
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
print(num1>=num2)
 
 # THANKYOU 