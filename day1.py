#Day1
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print("Day 1 - String Manipulation",'String Concatenation is done with the "+" sign.','e.g. print("Hello " + "world")',"New lines can be created with a backslash and n.",sep="\n")
print(len(str(input("What is your name? "))))
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
a,b=b,a
print(a,b)
#project1
print("welcome to band name generator.")
city=input("Which city did you grow up in ?\n")
pet=input("name of your pet ?\n")
print("Your band name could be " + city + " " + pet)
