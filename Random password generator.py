import random
from tkinter import *
import pyperclip
import string

def generator():
    small = string.ascii_lowercase
    capitals = string.ascii_uppercase
    numbers=string.digits
    special=string.punctuation

    all = small + capitals + numbers + special
    password_length = int(length_Box.get())
    
    password = random.sample(all, password_length)
    passwordField.insert(0,password)

def copy():  #used to copy the code
    random_password=passwordField.get()
    pyperclip.copy(random_password)

#creating an window using tkinter
root = Tk()
choice=IntVar()
root.title('****Password Generator***')
root.geometry('500x450')
root.config(bg='black')

choice=IntVar()
Font=('arial',13,'bold')

lengthLabel=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)#to specify the lenght of the code
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)#to get the password
passwordField.grid()

#creating a copy button
copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

    
root.mainloop()