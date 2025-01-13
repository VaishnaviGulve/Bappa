# oops = object oriented programming system
# to map witk real world senarios, we started using objects in code.

# Class & object in python
# class is a blueprint for creating objects

from typing import Any

class student:
    name = "vaishnavi"

s1 = student()  
print(s1)

class car:
    color = "blue"
    brand = "mercedes"

car1 = car()
print(car1.color)
print(car1.brand)

# _ _ init _ _ function :
# constructor = object creation 
# this funtion always being executed when the class is being initiated. 

class student:
    name = "vaishnavi pradip gulve"
    def __init__(self):
       print(self) 
       pass

s1 = student 
print(s1.name)

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new studnt in database..")

s1 = student("karan",97.77)
print(s1.name,s1.marks)
        
#Class & Attributes Attrinutes 

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("hello")
    
    def get_marks(self):
        return self.marks
    
a1 = student("karan",97.77)
a1.hello()
print(a1.get_marks())

# PRACTICE QUESTION

# Create the student class that takes name & marks of three subjects as arguments in constructor. then create a method to print the average.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for values in self.marks:
            sum+=values
        print("hi",self.name, "your avg score is :",sum/3)

s1 = student("tonystark", [99,98,97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

# Static Methods
# methods that don't use self parameter
# they can't access or modify class state & generally for utility.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for values in self.marks:
            sum+=values
        print("hi",self.name, "your avg score is :",sum/3)

s1 = student("tonystark", [99,98,97])
s1.get_avg()
s1.hello()

# Two pillars of OOPs:

# 1)Abstraction:
#     - Hiding the implimentation details of a class and only showing the essentiao features to the users.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 =  Car()
car1.start()

# 2)Encapsulation: 
#     - Wrapping data andd functions into a single unit (object).

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance =", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

# THANKYOU
