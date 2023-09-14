#Day2
two_digit_number = input("Type a two digit number: ")
two_digit_number1 = str(two_digit_number)
print(int(two_digit_number1[0])+int(two_digit_number1[1]))

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height=float(height)
weight=float(weight)
print(int(weight//(height*height)))

age = input("What is your current age? ")
age=int(90-int(age))
print("You have ", age*365,"days ", age*52, "weeks, and ", age*12, " months  left")

a = float(input("What was the total bill ?"))
b = int(input("How much tip do you want to give 10,12 or 15?"))
c = int(input("How many people are splitting the bill?"))
a= a+((b*a)/100)
a= a/c
print(a)