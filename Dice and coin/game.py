import random
from tkinter import *
import cv2
from PIL import ImageTk, Image

root=Tk()
root.title("Games")
root.geometry("500x500+0+0")

def Roll_a_dice():
    dice=random.randint(1,6)
    global img1
    if(dice==1):
        img1 = ImageTk.PhotoImage(Image.open("dice1.jpg"))
        Label(root,image=img1).grid(row=1,column=0)
    elif (dice==2):
        img1 = ImageTk.PhotoImage(Image.open("dice2.png"))
        Label(root,image=img1).grid(row=1,column=0)
    elif (dice==3):
        img1 = ImageTk.PhotoImage(Image.open("dice3.png"))
        Label(root,image=img1).grid(row=1,column=0)
    elif (dice==4):
        img1 = ImageTk.PhotoImage(Image.open("dice4.jpg"))
        Label(root,image=img1).grid(row=1,column=0)
    elif (dice==5):
        img1 = ImageTk.PhotoImage(Image.open("dice5.png"))
        Label(root,image=img1).grid(row=1,column=0)
    elif (dice==6):
        img1 = ImageTk.PhotoImage(Image.open("dice6.png"))
        Label(root,image=img1).grid(row=1,column=0)


def Toss_coin():
    coin=random.randint(1,2)
    global img1
    if(coin==1):
        img1 = ImageTk.PhotoImage(Image.open("heads.jpg"))
        Label(root,image=img1).grid(row=1,column=0)
        #print("The coin result of coin tossed is Heads")
    elif(coin==2):
        img1 = ImageTk.PhotoImage(Image.open("tails.jpg"))
        Label(root,image=img1).grid(row=1,column=0)
        #print("The coin result of coin tossed is Tails")

Button(root,text="Roll a Dice",command=Roll_a_dice).grid(row=0,column=0,padx=10,pady=10)
Button(root,text="Toss A Coin",command=Toss_coin).grid(row=0,column=1,padx=10,pady=10)





     
root.mainloop()



    

