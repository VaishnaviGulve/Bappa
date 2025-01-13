# STTRINGS
# It is a data type that stores a sequence of characters 

str1 = "this is a string" # mainly use 
str2 = 'apna college'
str3 = """MCOERC"""

str = "this is string.\n we ae creating it in python." 
print(str)

# Basic Operations

# 1. concatination
#   "hello" + "world " -> "helloworld"
str1 = "Apna"
str2 = "college"
print(str1+str2)
print(str1+" "+str2)

# 2. length of str 
#    len(str)
str = "apnacollege"
print(len(str))
print(len(str1+" "+str2))

# Indexing 
# starts from 0
vish = "apna college"
print(vish[2])

# Slicing - positive indexing
# accesing part of string 
# str[starting_idx : ending_idx]
# ending idx is not included
str = "Apna college"
print(str[1:4])
print(str[:4]) # [0:4]
print(str[1:]) # [1:len(str)]

#slicing - negative indexing 
str = "apple"
print(str[-1:-4])
print(str[:-1])
print(str[-5:])

# string functions 
str5 = "I am a coder."
print(str5.endswith("er."))
print(str5.capitalize())
print(str5.replace("o","a")) 
print(str5.find("I"))
print(str5.count("am"))

# PPACTICE QUESTIONS

# WAP to input user's first name & print its length.
name = input("enter your name = ")
print(len(name))

# WAP to fint the occurence of '$'in a string.
str = "Hi,$I am the $ symbol $99.99"
print(str.count("$"))

# CONDITIONAL STATEMENTS
# if-elif-else (syntax)
# if(condition):
#    statement1
# elif(condition):
#    statement2
# else:
#    statementN

age = 16 
if(age>=18):
    print("can vote & apply for license")
    print("can drive")
else:
    print("your are not able")

num = 5 
if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")
else:
    print("number is different")

marks = 80
if(marks>=90):
    print("grade = A")
elif(marks>=80):
    print("grade = B")
elif(marks>=70):
    print("grade = C")
else:
    print("grade = D")

# Nesting
age = 34
if(age>=18):
    if(age>=80):
        print("cannot drive ")
    else:
        print("can drive")
else:
    print("cannot drive")

# PRACTICE QUESTIONS

# WAP to check if a number entered by the user is odd or even 
num = int(input("enter a num = "))
if(num % 2):
    print("num is even ")
else:
    print("num is odd ")

# WAP to find the greatest of three numbers entered by the users
a = int(input("enter a num1 = "))
b = int(input("enter a num2 = "))
c = int(input("enter a num3 = "))
if(a>b):
    if(b>c):
        print("a is greater")
    elif(c>a):
        print("c is greater")
    else:
        print("both are small")
else:
    print("b is greater")

# WAP to check if a number is a muliple of 7 or not
num = int(input("enter a num = "))
if(num%7==0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7\n")

# f. string :
# use for string formating :

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Vaishnavi"
print(letter.format(name,country))
print(f"\nHey my name is {name} and I am from {country}")
print(f"\nWe use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"\nfor only {price:.2f} dollars!"
print(txt)
print(type(f"{2 * 30}"))
print(f"{2 * 30}")

# Docstring :
# they are the string literals that appear right after the definition of a function, modules, methods or class.

def square(n):
    '''\nTakes in a number n, returns the square of n.'''
    print(n**2)
print(square.__doc__)
square(5)

import this
print("\nThe Zen of Python, by ~ Tim Peters")

print("\nBeautiful is better than ugly.")
print("Explicit is better than implicit.")
print("Simple is better than complex.")
print("Complex is better than complicated.")
print("Flat is better than nested.")
print("Sparse is better than dense.")
print("Readability counts.")
print("Special cases aren't special enough to break the rules.")
print("Although practicality beats purity.")
print("Errors should never pass silently.")
print("Unless explicitly silenced.")
print("In the face of ambiguity, refuse the temptation to guess.")
print("There should be one-- and preferably only one --obvious way to do it.")
print("Although that way may not be obvious at first unless you're Dutch.")
print("Now is better than never.")
print("Although never is often better than *right* now.")
print("If the implementation is hard to explain, it's a bad idea.")
print("If the implementation is easy to explain, it may be a good idea.")
print("Namespaces are one honking great idea -- let's do more of those!")

# short hand if else statement;
a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")
print(9) if a>b else ""

c = 9 if a>b else 0 
print(c)

# THANKYOU