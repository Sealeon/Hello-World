from tkinter import *
from tkinter import messagebox

patience = 3

def message():
    global patience
    if patience != 0:
        patience -= 1
        messagebox.showwarning("This is", "Hello world!")
    else:
        messagebox.showerror("You know what?", "Forget about it,\nI'm leaving!")
        root.destroy()

root = Tk()
text = Label(root, text = "This is not a greeting", pady = 5, padx = 15)
button = Button(root, text = "Pardon?", command = lambda:message())
text.grid(row = 0, column = 0)
button.grid(row = 1, column = 0)
root.mainloop()
