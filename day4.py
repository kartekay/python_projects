#Day4
import random as r
num=r.randint(0,1)
if num==1:
    print("Heads")
else:
    print("Tails")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
import random
a=random.randint(0,len(names)-1)
print(names[a],"is going to buy the meal!")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
l1=[]
for i in position:
    l1.append(int(i))
map[l1[0]][l1[1]]='x'
print(f"{row1}\n{row2}\n{row3}")

import random
a=int(input("Type 0 for rock,1 for paper and 2 for scissors "))
b=random.randint(0,2)
if b-a==1 or b-a==-2:
    print("Computer won")
elif a==b:
    print("Draw")
else:
    print("You won")
