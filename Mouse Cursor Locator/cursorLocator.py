import pygame
import pyautogui
from tkinter import *
from tkinter import colorchooser,messagebox


#Initialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((600,100))


#Title And Icon
pygame.display.set_caption("Mouse Position Locator")

font = pygame.font.Font('freesansbold.ttf',32)



def msgBox(X,Y):
    text = font.render("Mouse Cursor at X = {}, Y = {}".format(str(X),str(Y)), True,(0,0,0))
    Xcord = font.render("Mouse X co-ordinate = " + str(X),True,(0,0,0))
    Ycord = font.render("Mouse Y co-ordinate = " + str(Y),True,(0,0,0))
    
    screen.blit(text, (15,25)) 
    # screen.blit(Xcord,(10,10))
    # screen.blit(Ycord, (10,50))


running = True

while running:

    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False




    mouseX,mouseY = pyautogui.position()

    msgBox(mouseX,mouseY)

    if mouseX == 1344 and mouseY == 5:
        pyautogui.click()
        print("Hello")

    pygame.display.flip()



