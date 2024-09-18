#Day5

student_heights = input("Input the student heights with space ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
a=0
for i in student_heights:
    a+=i
b=(a/len(student_heights))
print(round(b))

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
student_scores.sort()
print(student_scores[len(student_scores)-1], "is the highest score in the class.")

j=0
for i in range(1,101):
    if i%2==0:
        j+=i
print(j)

import random
a=random.randint(1,100)
print(a)
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
for i in range(0,nr_letters):
    a=letters[random.randint(0,len(letters)-1)]
    password=password+str(a)
for j in range(0,nr_symbols):
    b=symbols[random.randint(0,len(symbols)-1)]
    password=password+str(b)
for z in range(0,nr_numbers):
    c=numbers[random.randint(0,len(numbers)-1)]
    password=password+str(c)
print("Your password is:",password)

