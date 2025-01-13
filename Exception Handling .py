# Exception handling :
try:
    num = int(input("enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer.")
except IndexError:
    print("IndexError")

# Finally Clause :
def func1():
    try:
        l = [1,2,3,4,5,6,7]
        i = int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x = func1()
print(x)

# Raising custom error :
# In python, we can use raise custom errors by using the 'raise' kwyword.

salary = int(input("enter salary amount : "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# Thankyou