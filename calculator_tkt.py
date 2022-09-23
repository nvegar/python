from logging import root
from sqlite3 import Row
from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=20)
e.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# e.insert(0, "Enter your name: ")

def button_add():
    return()

button_1 = Button(root, text=1, padx=40, pady=20, command=button_add)
button_2 = Button(root, text=2, padx=40, pady=20, command=button_add)
button_3 = Button(root, text=3, padx=40, pady=20, command=button_add)
button_4 = Button(root, text=4, padx=40, pady=20, command=button_add)
button_5 = Button(root, text=5, padx=40, pady=20, command=button_add)
button_6 = Button(root, text=6, padx=40, pady=20, command=button_add)
button_7 = Button(root, text=7, padx=40, pady=20, command=button_add)
button_8 = Button(root, text=8, padx=40, pady=20, command=button_add)
button_9 = Button(root, text=9, padx=40, pady=20, command=button_add)
button_0 = Button(root, text=0, padx=80, pady=20, command=button_add)
button_dot = Button(root, text=".", padx=40, pady=20, command=button_add)
button_sum = Button(root, text="+", padx=40, pady=20, command=button_add)
button_sus = Button(root, text="-", padx=40, pady=20, command=button_add)
button_mul = Button(root, text="*", padx=40, pady=20, command=button_add)
button_div = Button(root, text="/", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="AC", padx=40, pady=20, command=button_add)
button_per = Button(root, text="%", padx=40, pady=20, command=button_add)
button_sym = Button(root, text="+/-", padx=40, pady=20, command=button_add)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_sum.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sus.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_clear.grid(row=1, column=0)
button_sym.grid(row=1, column=1)
button_per.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_0.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=3)
button_dot.grid(row=5, column=2)



root.mainloop()

