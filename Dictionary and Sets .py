# DICTIONARY 
# Used to store data values in key value pairs
# They are unordered, mutable (changeable) & don't allow duplicate keys 
Dict = {"name":"vaishnavi","age":"18"}
# always write in "key":"value" pair
print(Dict)

info = {
    "name":"apnacollege",
    "subject":["python","java","c++"],
    "age":18,
    "is_adult":True,
    "marks":8.86
}
print(info)
print(info["name"])

info["age"]=19
print(info)

null_dict = {}
null_dict["name"]="vaishnavi"
print(null_dict)

# Dictionary methods
d = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i"}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("keys"))
print(d.update({"newdict":"i"}))
print(d)

# Sets in python
# Set is collection of unordered items.
# Each element in the set must be unique and immuttable. 
# in sets repeat number only stored once
d = {1,2,3,4,3,2,1,3,2,5,6}
print(d)

collection = {1,2,3,4,5,6,7,7}
print(collection)
print(type(collection))
print(len(collection))

null={}
print(null)
print (type(null))

# Sets method 
collection = {1,2,3,4,5,6,7,7}
print(collection.add(8))
print(collection)
print(collection.remove(5))
print(collection)
print(collection.clear())
print(collection)
collection = {1,2,3,4,5,6,7,7}
print(collection.pop())
print(collection)

set1={1,2,3}
set2={2,3,4}
print(set1)
print(set2)
print(set1.union(set2))
print(set2.union(set1))
print(set1.intersection(set2))
print(set2.intersection(set1))

# LET'S PRACTICE 

# Store following word meanings in a python dictionary :
# table : "a piece of furniture"'"list of facts & figures"
# cat : "a small animal"
dict = {"cat":"a small animal",
        "table":["a piece of furniture","list of facrts & figures"]}
print(dict)

# You are given a list of subjects for students. Assume one classrom is required for 1 subject. How many classrooms are needed by all students. 
students ={
"python","java","C++","javascript","python",
"java","python","java","C++","c"
}
print(len(students))

# WAP to enter marks of 3 subjects from the users and store them in a dictionary. Start with an empty dictionary &add one by one. Use subjects name as key &marks as value.
marks = {}
x = int(input("enter phy marks : "))
marks.update({"phy": x})
y = int(input("enter chem marks : "))
marks.update({"chem": x})
z = int(input("enter maths marks : "))
marks.update({"maths": z})
a = int(input("enter bxe marks : "))
marks.update({"bxe": a})
b = int(input("enter graphics marks : "))
marks.update({"graphics": b})
print(marks)

# figure out a way to store 9 & 9.0 as separete values in the set.( you can take help of built-in data types )
values = {9,9.0}
print (values)

values = {("int",9),("float",9.0)}
print(values)