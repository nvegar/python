from tkinter import *
root = Tk()

#variable is stored in the root object
root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
        
b = Button(root, text="Click Me", command=clicked)
b.pack()

L = Label(root, text="No clicks yet.")
L.pack()

root.mainloop()

def clicked():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
    
    #create a new label after 20 clicks
    if root.counter > 20:
        hyper = Label(root, text="Hyper Mode!")
        hyper.pack()
        
        #change the click function after 20 clicks
        b.config(command = hyper_click)
    

def hyper_click():
    root.counter = int(1.08 * root.counter)
    L['text'] = 'Button clicked: ' + str(root.counter)


b = Button(root, text="Click Me", command=clicked)
b.pack()

L = Label(root, text="No clicks yet.")
L.pack()