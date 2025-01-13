# File I/O in python:
# Python can be used as to perform operations pn a file. (read and write data)

# Types of all Files 
# 1. Text files : txt, .docx, .log etc 
# 2. Binary files : .mp4, .mov, .png, .jpeg etc 

# Open , Read & Close File:
# f = open("file_name","mode")
# mode = read or write 

# 'r' = open for reading (default).
# 'w' = open for writing, truncating the file first.
# 'x' = create a new file and open it for writing.
# 'a' = open for writing, appending to the end of the file if exists.
# 'b' = binary mode.
# 't' = text mode.
# '+' = open a disk filefor updating (reading and writing).

# Reading a file: 
# data = f.read()         reads entire file
# data = f.readline()     reads one line at a time

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt","r")
line1 = f.readline()
print(line1)
print(type(line1))
f.close()

# Writing to a file :
f = open("demo.txt","w")
f.write("I want to learn Javascript")
f.close()

f = open("demo.txt","a")
f.write("Then I will move ReactJS")
f.close()

f = open("sample.txt","a")
f.close()

f = open("demo.txt","r+")   # overwrite from starting, no truncate.
f.write("abc")
print(f.read())
f.close()

f = open("demo.txt","w+")   # truncate
f.write("abc")
print(f.read())
f.close()

f = open("demo.txt","a+")   # overwrite from ending, no truncate.
f.write("abc")
print(f.read())
f.close()

# with syntax
with open("demo.txt","r")as f:
    data = f.read()
    print(data)

with open("demo.txt","w")as f:
    f.write("new data")

# Deleting a file
# using the os module
# Module (like a code library) is a file written by another programmer that generally has a functions we can use.
#      import os
#      os.remove(filename)

import os
os.remove("sample.txt")

# PRACTICE QUESTIONS:

# Create a new file "practice.txt" using python. add the following datain it:
# [ Hi everyone. we are learning file I/O using java. i like programming in java.]
with open("practice.txt",'w') as f:
  f.write("Hi everyone.\n we are learning file I/O \n using java.\n I like programming in java.")  

# WAF that replace all occurences of "java" with "python" in the above file.
with open("practice.txt",'r') as f:
   data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("practice.txt",'w') as f:
   f.write(new_data)

# Search if the word "learning" exists in the python. 
def check_for_word():
  with open("practice.txt","r") as f:
       data = f.read()
       if(data.find("learning") != -1):
          print("found")
       else:
          print("not found") 
        
check_for_word()

# WAF to find in which line of the file does the word "learning" occur first. Print-1 if word not found.
def check_for_line():
   word ="learning"
   data = True
   line_no = 1
   with open("practice.txt","r")as f:
      while data:
         data = f.readline()
         if(word in data):
            print(line_no)
         line_no += 1   

   return -1

check_for_line()
      
# From a file containing numbers separated by comma, print the count of even numbers.
with open("practice.txt","r")as f:
   data = f.read()
   print(data)

   num = ""
   for i in range(len(data)):
      if(data[i] == ","):
         print(int(num))
         num = ""
      else:
         num += data[i]

# OR
count = 0
with open("practice.txt","r")as f:
   data = f.read()

   nums = data.split(",")
   for val in nums:
      if(int(val) % 2 == 0):
         count += 1

print(count)


# THANKYOU            