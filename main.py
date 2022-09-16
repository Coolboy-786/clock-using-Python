# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=("ds-digital",80),background = "cyan", foreground = "red")
label.pack(anchor='center')
time()

mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
