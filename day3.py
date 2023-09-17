#Day3
nu = int(input("Which number do you want to check? "))
a= nu%2
if a==1:
    print("This is an odd number.")
else:
    print("This is an even number.")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
a = (weight/height**2)
if a<18.5:
    print("Your BMI is ",round(a),", you are underweight.")
elif a>=18.5 and a<=25:
    print("Your BMI is ",round(a),", you have a normal weight.")
elif a>25 and a<=30:
    print("Your BMI is ",round(a),", you are slightly overweight.")
elif a>30 and a<=40:
    print("Your BMI is ",round(a),", you are obese.")
else:
    print("Your BMI is ",round(a),", you are clinically obese.")

year = int(input("Which year do you want to check? "))
if year%400==0:
    print("is leap year.")
elif year%4==0:
    if year%100==0:
        print("not leap year")
    else:
        print("is leap year")
else:
    print("Not leap year.")

print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
cost=0
if size=="L":
    cost+=25
    if add_pepperoni=="Y":
        cost+=3
elif size=="M":
    cost+=20
    if add_pepperoni=="Y":
        cost+=3
else:
    cost+=15
    if add_pepperoni=="Y":
        cost+=2
if extra_cheese=="Y":
    cost+=1
print("Your final bill is: $",cost)

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
count1=0
count2=0
string=name1.upper()+name2.upper()
list1=["T","R","U","E"]
list2=["L","O","V","E"]
for i in string:
    for j in list1:
        if i==j:
           count1+=1
    for k in list2:
        if i==k:
           count2+=1
count3 = int(str(count1)+str(count2))
if count3<=10 or count3>=90:
    print("Your score is ","**"+str(count1)+str(count2)+"**,","you go together like coke and mentos.")
elif count3>=40 and count3<=50:
    print("Your score is ","**"+str(count1)+str(count2)+"**,","you are alright together.")
else:
    print("Your score is ","**"+str(count1)+str(count2)+"**.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
a=input("Which direction do you want to go? ",'Type "left" or "right"  ')
if a=="left":
    b=input("'swim' or 'wait'")
    if b=="wait":
        c=input("yellow,red or blue")
        if c=="yellow":
            print("you win")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")