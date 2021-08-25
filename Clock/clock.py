from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
root.geometry("180x80")
# root.resizable(False,False)
root.configure(background = '#999')

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root,font='consolas 20 bold',background = '#999',foreground = '#111')

lbl.grid(row = 2, column = 4)
time()

mainloop()