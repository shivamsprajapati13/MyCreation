import pygame
from time import *
import time

#Initialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((600,100))


#Title And Icon
pygame.display.set_caption("StopWatch")

font = pygame.font.Font('freesansbold.ttf',32)


def showClock(h,m,s):
	text = font.render("Time: {}.{}.{} ".format(int(h-12),str(m),str(s)), True,(0,0,0))
	screen.blit(text, (15,25)) 


# x = time.localtime()
running = True
while running:
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running = False

	x = time.localtime()
	hour = x.tm_hour
	minutes = x.tm_min
	second = x.tm_sec
	showClock(hour,minutes,second)
	
	pygame.display.flip()
	

