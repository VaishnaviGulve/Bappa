# Functions in Python
# Block of statements that are perform a specific task.

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum

calc_sum(5,10)
calc_sum(2,20)

def print_hello():
    print("hello")

print_hello()    
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(1,2,3)

# Two types of fuctions:

# 1) Built in functions: 
#     - print(),len(),type(),range()...

# 2) User defined functions:
#     - functions written by programers.

# Default parameters:
# Assigning a default value to parameter, which is used when no argument is passed. 

def calc_prod(a=1,b=1):
    print(a*b)
    return a*b
calc_prod()

# enumerate function :
marks = [12,56,32,98,12,45,1,4]
idx = 0
for mark in marks:
    print(mark)
    if(idx == 3):
        print("Vish, awesome!")
    idx += 1
# or
marks = [12,56,32,98,12,45,1,4]

for index, mark in enumerate(marks):
    print(mark)
    if(idx == 3):
        print("Vish, awesome!")
    idx += 1

# PRACTICE QUESTIONS

# WAF to print the length of a list.(list is the parameter)
num = [1,2,3,4,45,45,33,12,34,43,21,67,87,98,897,67]
def print_len(list):
    print(len(list))

print_len(num)

# WAF to print the elements of a list in a single line.(list is the parmeter)
heroes = ["thor","ironman","captain america","shaktiman"]
print(heroes[0], end=" ")
print(heroes[1], end=" ")

def print_list(list):
    for item in list:
        print(item, end= " ")

print (list(heroes))

# WAF to find the factorial of n.(n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    print(fact)

calc_fact(5)
    
# WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val,"USD =",inr_val,"INR")

converter(50)

# RECURSION 
# when a function calls itself repeatedly.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(3)

def fact(n):
    if(n == 0 or n==1):
        return 1
    else :
        return n * fact(n -1)
    
print(fact(78))

# PRACTICE QUESTIONS

# Write a recursive function to calculate the sum of first n natural number.
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

# Write a recursive function to print all elements in a list.
# Hint:use list and index as a parameter.
def print_list(list,index=0):
   if(index ==len(list)):
       return
   print(list[index])
   print_list(list,index+1)

fruits =["mango","apple","banana","orange"]
print_list(fruits)

# THANKYOU