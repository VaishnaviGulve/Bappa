import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)


import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter hour = "))
print(hour)

if(hour>=0 and hour<12):
    print("GOOD MORNING SIR!")
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON SIR!")
elif(hour>17 and hour<0):
    print("GOOD NIGHT SIR!")
else:
    print("NONE")

# Create a program capable of displaying questions top the users like KBC.
Questions =[
    ["which language was use to create facebook",
     "python","jacasript","PHP","none",3],
    ["Current Railway Minister of India is",
     "Mamta Banarjee","Ram Vilash","Ashwini Vaishnaw","Piyush Goyal",3],
    ["Which god is also known as 'Gauri Nandan'?",
      "Agni","Indra","Hanuman","ganesha",4]
    ]
levels = [1000,2000,3000,4000,6000,8000,10000]
i = 0 
money = 0
for i in range(0,len(Questions)):
    question = Questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]}")
    reply = int(input("Enter your answer(1-4) or press 0 if you have to quite\n"))
    if (reply ==0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer,You have won Rs. {levels[i]}")
        if(i == 3):
           money = 10000
        elif(i == 9):
            money = 15000
        elif(i == 12):
            money = 20000
    else:
        print("Wrong answer")
        break

print("\nKaun Banega Crorepati Exercise is completed..")

# Write a python program to translate a message into secret code language .

st = input("enter a msg ")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding ")
coding = True if (coding == 1 )else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "DSF"
            r2 = "JKR"
            stnew = r1+ word[1:] +r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(words))

