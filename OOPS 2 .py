# del keyword
# used to delete object properties or object itself.

class student:
    def __init__(self,name):
        self.name = name

s1 = student("vaishnavi")
print(s1.name)
# del s1.name
# print(s1.name)

# Private (like) attributes & methods.
# conceptual implimentation in pythonp -
# they are meant to used only within the class and are not accesible from outside the class.

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def __hello(self):
        self.__hello() 

p1 = Person()

# INHERITANCE -
# when one class drives the properties & methods of another class. 

# types of inheritence :

# 1) single inheritence.
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..") 

class toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

# 2) multi-level inheritence.

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..") 

class toyotacar(car):
    def __init__(self,brand):
        self.name = brand

class Fortuner(toyotacar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

# 3) multiple inheritence.

class A:
    varA = " welcome to class A"

class B:
    varB = " welcome to class B"

class C(A,B):
    varC = " welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

# Super method:
# super() method is used to access methods of the parent class.

class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..") 

class toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
       
car1 = toyotacar("prius","electric")
print(car1.type)

# Class method:
# it is bound to the class and receives the class as an implicit first argument.

class person:
    name = "ANONYMOUS"

    def changename(self,name):
        self.name = name
#or
    def changename(self,name):
        person.name = name
#or
    def changename(self,name):
        self.__class__.name ="karan"
#or
    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("karan gulve")
print(p1.name)
print(person.name)

# Property
# we use @property decorator on any method in the class to use the method as a property.

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
            return str((self.phy + self.chem + self.math) / 3) + "%"
        
s1 = student(99,98,97)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)

# POLYMORPHISM : Operator Overloading
# when the same operator is allowed to have different meaning according to the context.

# Operators & Dunder functions - 
# a+b  = a.__add__(b)
# a-b  = a.__sub__(b)
# a*b  = a.__mul__(b)
# a/b  = a.__truediv__(b)
# a%b  = a.__mod__(b)
# a>b  = a.__gt__(b)

class Complex:
    def __init__(self, real ,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i + ",self.img,"j")
    
    def __add__(self,n2):
        newreal = self.real + n2.real
        newimg = self.img + n2.img
        return Complex(newreal,newimg)

    def __sub__(self,n2):
        newreal = self.real - n2.real
        newimg = self.img - n2.img
        return Complex(newreal,newimg)
    
n1 = Complex(1,3)
n1.shownumber()

n2 = Complex(2,4)
n2.shownumber()

n3 = n1 + n2
n3.shownumber()

n4 = n1 - n2
n4.shownumber()

# PRCTICE QUESTION

# Define a circle class to create a circle with radius r using the constructor.
# Define an area() method of the class which calculates the area of the circle. 
# Define a perimeter() method of the class which allows you to calculate th perimeter of the circle.

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = circle(21)
print(c1.area())
print(c1.perimeter())

# Define a employee class with attributes role, department & salary. this class also has a showdetails() method.
# Create an engineer class that inherit  properties from employees & has additional attributes : name & age.  

class employee:
    def __init__(self,role , dept, salary ):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept )
        print("salary = ", self.salary)

class engineers(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT","75,000")

e1 = employee("accountant","finance","60,000")
e1.showdetails()  

engg1 = engineers("sanket",20,)
engg1.showdetails()

# Create a class called order which stores item & its price.
# Use dunder function __gt__() to convey that:
#         order1 > order2 if price of order1 > price of order2.

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,o2):
        return self.price > o2.price
    
o1 = order("chips",20)
o2 = order("tea",15)

print(o1 > o2)

# THANKYOU
