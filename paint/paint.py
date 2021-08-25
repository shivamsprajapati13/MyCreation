from tkinter import *
import pyautogui
from PIL import ImageTk, Image
import cv2 as cv
from tkinter import colorchooser,messagebox


canvas_width = 500
canvas_height = 500

color = "#000000"
class paintSurface:
	def choose_color(self):
		global color
		color = (colorchooser.askcolor(title ="Choose color")[1])
		
	def paint(self,event):
		currentX1,currentY1 = (event.x-1),(event.y-1)
		currentX2,currentY2 = (event.x+1),(event.y+1)
		cnv.create_line(currentX1, currentY1, currentX2, currentY2, fill = color, capstyle = ROUND, smooth = TRUE, splinesteps = 36, width = 5.0)

root = Tk()
root.geometry("800x600")
root.title( "Painting " )
cnv = Canvas(root, width = canvas_width,height = canvas_height, bg = "#FFFFFF")


ps = paintSurface()

cnv.pack(expand = YES, fill = BOTH) 
cnv.bind( "<B1-Motion>", ps.paint )
#cnv.bind("<Double-1>", choose_color)

colorbutton = Button(root,padx=5,pady=5, width = "30",text = "Choose Color", command = lambda  : ps.choose_color())
colorbutton.pack()

message = Label( root, text = "To draw, press and drag the mouse" )
message.pack( side = BOTTOM )
    
root.mainloop()

