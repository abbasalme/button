#import from tkinter library 
import tkinter as tk

#create button click function
def button_click():
    print("Button Clicked")

#create root window, name root title
root = tk.Tk()
root.title("Button Example")

#create button object, create three arguement paramater
button = tk.Button(root,text="Click Me!",command=button_click)
button.pack()

#create mainloop to open window root
root.mainloop()