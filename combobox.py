#import from tkinter library 
import tkinter as tk
from tkinter import ttk 

#create function which handles the event for the combobox, then after selecting an item print selected item
def on_select(event):

    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#create root window and title for root window 
root = tk.Tk()
root.title("Combobox Example")

#create array item list
items =["Item 1", "Item 2", "Item 3", "Item 4"]

#create the comboboxobject 
combo_box = ttk.Combobox(root, values=items)

#bind the selected event with the combobox function 
combo_box.bind("<<ComboboxSelected>>", on_select)
combo_box.pack()

root.mainloop()

