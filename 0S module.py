# os module:
import os

#if (not os.path.exists("data")):
#    os.mkdir("data")
 
#for i in range(0,100):
#    os.mkdir(f"data/day{i+1}")

#for i in range(0,100):
#    os.rename(f"data/ Tutorial{i+1}",f"data/ Tutorial {i+1}")

import os
folders = os.listdir("data")
print(folders)

print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    

# use os.system to learn mpre methods of os moodule :
