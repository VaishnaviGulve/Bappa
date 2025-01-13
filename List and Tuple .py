# LIST
# list are muttable. they can be changed.
# A built in data type that stores set of values
a = [1,2,3,4,5,6]

marks = [45,45,23,56,67]
print(marks)
print(type(marks))
print(len(marks))

# indexing
print(marks[0])
print(marks[4])

student = ["karan", "vaishnavi", "dipali", 65,76.78]
print(student)
student[0] = "pradip"
print(student)

# Slicing
marks = [45,45,23,56,67]
print(marks[0:4])
print(marks[-1:-5])

# list methods
list = [1,2,3,4,56,78,89,5,6,7,8,9,12,23]
print(list.append(4))
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)
print(list.reverse())
print(list)
print(list.insert(1,5))
print(list)
print(list.remove(1))
print(list)
print(list.pop(2))
print(list)

# TUPLES 
# immutable sequence of value

tup = (23,13,5,78,89,90,98)
print(tup[0])
t = ()
print(t)
print(type(tup))
print(tup[1:4])
tup = (23,13,5,78,89,90,98)
print(tup.index(23))
print(tup.count(89))

# PRACTICE QUESTIONS

# WAP to ask the user to enter names of their 3 favorite movies and store them in a list 
movies = []
movie1 = input("enter your 1st movie")
movie2 = input("enter your 2nd movie")
movie3 = input("enter your 3rd movie")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# WAP to check if a list contains a palindrome of elements. (hint: use copy.()method)
list1 = [1,2,3]
list2 = [1,2,1]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple. 
tup = ["C","D","A","A","B","B","A"]
print(tup.count("A"))

# Store the above values in list & sort them from "A" & "D". 
list = (tup)
print(list)

# THANKYOU

