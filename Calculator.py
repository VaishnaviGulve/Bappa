# simple calculator in python

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=",multiply(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

else:
    print("Invalid Input")


