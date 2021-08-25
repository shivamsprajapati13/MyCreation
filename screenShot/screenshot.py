from time import sleep
from PIL import ImageGrab
import pyautogui
from tkinter import Tk, Label, Radiobutton, StringVar, Button, messagebox, Frame
import random
import string
from datetime import date
from datetime import datetime


def on_enter(e):
    b1['background'] = '#033500'
    b1['foreground'] = 'white'


def on_leave(e):
    b1['background'] = '#3cb043'
    b1['foreground'] = 'black'

def TakeShoot():
	today = date.today()
	now = datetime.now()


	file_name1 = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
	# d3 =  today.strftime("%B %d %Y")
	d3 = now.strftime("%d_%m_%Y_%H_%M")
	file_name = d3+file_name1
	# print(file_name)
	if screenVal.get() == 'NA':
		messagebox.showinfo('Message','Select Your Screen Type')
	else:
		if screenVal.get() == 'ms_teams':
			root.withdraw()
			sleep(0.2)
			image = ImageGrab.grab(bbox = (9,103,1361,629))
			image.save("ms_teams_{}.png".format(str(file_name)))
			# print('ms_teams')
			root.deiconify()
		elif screenVal.get() == 'full_screen':
			root.withdraw()
			sleep(0.2)
			image = ImageGrab.grab()
			image.save("full_screen_{}.png".format(str(file_name)))
			root.deiconify()

		elif screenVal.get() == 'chrome':
			root.withdraw()
			sleep(0.2)
			image = ImageGrab.grab(bbox = (0,103,1374,729))
			image.save("chrome_{}.png".format(str(file_name)))
			root.deiconify()
			# print("Chrome")
	




root = Tk()
root.geometry("300x200")
root.title("Take Screenshot")
root.resizable(False,False)


Label(root,text = "Select Your Screen",font='consolas 14 bold').grid(row = 1, column = 2)

screenVal = StringVar()
screenVal.set('NA')
r1 = Radiobutton(root,text = "Full Screen",variable = screenVal,value = 'full_screen',font='consolas 14 bold').grid(row = 5,column = 2)
r2 = Radiobutton(root,text = "Microsoft Teams Screen",variable = screenVal,value = 'ms_teams',font='consolas 14 bold').grid(row = 8,column = 2)
r3 = Radiobutton(root,text = "Chrome Screen",font='consolas 14 bold',variable = screenVal,value = 'chrome').grid(row = 11,column = 2)



b1 = Button(root, text = 'Take Screenshot',command = TakeShoot,cursor = 'hand2',font='consolas 14 bold',)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)
b1.grid(row = 15,column = 2)

root.mainloop()



