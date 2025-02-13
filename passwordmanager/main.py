from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
tk=Tk()
tk.title("Password Manager")
tk.config(padx=20,pady=20)
canvas=Canvas(height=200,width=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

def generate_random_string():

    characters = string.ascii_letters + string.digits
    characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(7))

def save():
    website=wentry.get()
    email=eentry.get()
    password=pentry.get()
    is_ok=messagebox.askokcancel(title="Confirm",message="Save Password ?")
    if is_ok is True:
      wentry.delete(0,END)
      eentry.delete(0,END)
      pentry.delete(0,END)
      with open("data.txt","a") as data_file:
          data_file.write(f"{website}|{email}|{password}\n")
    else:
        pass

def password():
    a=generate_random_string()
    pentry.delete(0,END)
    pentry.insert(0,f"{a}")
    pyperclip.copy(a)
wlabel=Label(text="Website")
wlabel.grid(row=1,column=0)
elabel=Label(text="Email/Username")
elabel.grid(row=2,column=0)
plabel=Label(text="Password")
plabel.grid(row=3,column=0)
wentry=Entry(width=55)
wentry.grid(row=1,column=1,columnspan=2)
wentry.focus()
eentry=Entry(width=55)
eentry.grid(row=2,column=1,columnspan=2)
pentry=Entry(width=35)
pentry.grid(row=3,column=1)

genp=Button(text="Generate Password",command=password)
genp.grid(row=3,column=2)
add=Button(text="Add",width=45,command=save)
add.grid(row=4,column=1,columnspan=3)



tk.mainloop()