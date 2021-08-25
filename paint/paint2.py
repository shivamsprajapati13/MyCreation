from tkinter import *
import pyautogui
from PIL import ImageTk, Image
import cv2 
from tkinter import colorchooser,messagebox
import imutils

canvas_width = 500
canvas_height = 150
color = "#000000"
# class paintSurface:
# 	def choose_color(self):
# 		global color
# 		color = (colorchooser.askcolor(title ="Choose color")[1])
		
# 	def paint(self,event):
# 		currentX1,currentY1 = (event.x-1),(event.y-1)
# 		currentX2,currentY2 = (event.x+1),(event.y+1)
# 		cnv.create_line(currentX1, currentY1, currentX2, currentY2, fill = color, capstyle = ROUND, smooth = TRUE, splinesteps = 36, width = 5.0)


def paint(event):
	currentX1,currentY1 = (event.x-1),(event.y-1)
	currentX2,currentY2 = (event.x+1),(event.y+1)
	cnv.create_line(currentX1, currentY1, currentX2, currentY2, fill = color, capstyle = ROUND, smooth = TRUE, splinesteps = 36, width = 5.0)


def mouse_click(event, x, y,flags, param):
	print("HELLO WORLD")
	if event == cv2.EVENT_MOUSEMOVE:
		cv2.circle(frame,(x,y),10,(255,0,0),-1)
	

camera=cv2.VideoCapture(0)

root = Tk()
root.geometry("800x600")
root.title( "Painting " )
cnv = Canvas(root, width = canvas_width,height = canvas_height, bg = "#FFFFFF")


# ps = paintSurface()


cnv.pack(expand = YES, fill = BOTH) 
# cnv.bind( "<B1-Motion>", ps.paint )
#cnv.bind("<Double-1>", choose_color)    
while True:
	mouseX,mouseY = pyautogui.position()
	print(mouseX,mouseY)
	(grabbed,frame)=camera.read()
	frame=imutils.resize(frame,width=600)
	frame = cv2.flip(frame,1)
	cnv.bind('<B1-Motion>',paint)
	
	cv2.imshow("Frame",frame)
	key=cv2.waitKey(1)&0xFF
	if key==ord("q"):
		break

	root.mainloop()






