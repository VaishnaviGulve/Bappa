# Loops in python 
# are use to repeat instructions

count = 1
while count <= 5 : 
    print("hello")
    count += 1

i = 1
while i <= 500 : 
    print("world",i)
    i += 1

# print numbers from 1 to 5
i = 5 
while i >=1:
    print(i)
    i-=1

print("loop ended")    

# LETS PRACTICE

# Print numbers from 1 to 100.
i = 1
while i <= 100 : 
    print("world",i)
    i += 1

# print the numberfrom 100 to 1
i = 100
while i >= 1 : 
    print(i)
    i -= 1

# Print the multiplication table of a number n
i = 1 
while i<=10:
    print(2*i)
    i+=1

# print the elements of following list using a loop 
# (1,4,9,16,25,36,49,64,81,100)
i = 1
while i<=10:
    print(i*i)
    i+=1

# search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100) 
nums = (1,4,9,16,25,36,49,64,81,100) 
x = 36
i = 0 
while i<len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    else:
        print("finding")
    i += 1

print("end of loop")

# KEYWORDS
# Break : used to terminate the loop when encountered. 
# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration. 

i = 1 
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of the loop")

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
print("end of the loop")

# for geting odd number as output 
i = 0
while i <= 100:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
print("end of the loop")

# for getting even number as a outout
i = 0
while i <= 100:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
print("end of the loop")

# for getting table of a number
n = input("enter a number : ")
print(f"multiplication table of {n} is :")
for i in range (1,11):
    print(f"{int(n)}*{i} = {int(n)*i}")
print(f"the table of {n} is here")

# SEQUENCIAL TRANVERSAL
list = [1,2,3,4,5,6,7]
for num in list :
    print(num)

tuple = [12,13,14,15,16,27]
for num in tuple :
    print(num)

str = "apna college"
for char in str :
    print(char)
else:
    print("END")

str = "apnacollege"
for char in str :
    if(char == 'o'):
        print('o found')
        break
    print(char)
else:
    print("END")

# PRACTICE QUESTIONS

# Print the elements of the following list using a loop :
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)

# Search for a number x in this tuple using loop :
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100,49]
x = 49
index = 0
for el in nums:
    if(el == x):
        print("number found at index",index)
        break
    index += 1

# RANGE()
# this functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (bby default), and stops before a specified number.
seq = range(5)
for i in seq:
    print(i)

for i in range(2,101,2):
    print(i)
    
# PRACTICE QUESTIONS

# Print numbers from 1 to 100 :
for i in range(1,101):
    print(i)

# Print numbers from 100 to 1 :
for i in range(100,0,-1):
    print(i)

# Print the multiplication table of a number n :
n = int(input("enter number : "))
for i in range(1,11):
    print(n*i)

# PASS STATEMENT:
# pass is null statement that does nothing. It is used as a placeholder for futur code.
# for el in range(10):
#     Pass

for i in range(5):
    pass

if i >5:
    pass

print("some useful work")

# PRACTICE QUESTIONS

# WAP to find the sum of first n numbers. (using while)
n = 5
sum=0
i=1
while i <= n:
    sum += i
    i += 1
print("total sum = ",sum)

# WAP to find the factorial of first n numbers. (using for)
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("factorial = ",factorial)
# OR 
n = 6 
fact = 1 
for i in range(1,1+n):
    fact *= i
print("factorial = ",fact)

# THANKYOU 