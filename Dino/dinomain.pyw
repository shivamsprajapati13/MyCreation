import pygame
import random
import math
import time
from time import time,sleep
from tkinter import *
from  tkinter import messagebox



pygame.init()
screen=pygame.display.set_mode((800,600))
root=Tk()
root.withdraw()
clock = pygame.time.Clock()
background=pygame.image.load('back.png')

global score_value
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(X,Y):
	score=font.render("Score :"+str(score_value),True,(255,255,255))
	screen.blit(score,(X,Y))


#dragon
dragon=pygame.image.load('dragon.png')
dragonX=100
dragonY=318
y=200
isjump=False
jumpCount=10
v=10
m=1



#dragon mov
def dragon_mov(X,Y):
	screen.blit(dragon, (X,Y))


#obstacles
tree=[]
treeX=[]
treeY=[]
treeX_change=[]
num_tress = 1

for i in range(num_tress):
	tree.append(pygame.image.load('trees.png'))
	treeX.append(700)
	treeY.append(348)
	treeX_change.append(700)

def tree_obst(X,Y):
	screen.blit(tree[i],(X,Y))



#Collision
def isCollision(treeX,treeY,dragonX,dragonY):
	distance=math.sqrt((math.pow(treeX-dragonX,2))+(math.pow(treeY-dragonY,2)))

	if distance<34:
		return True
	else:
		return False
		
#GAME OVER
font2=pygame.font.Font('freesansbold.ttf',50)
text2X=400
text2Y=300

def game_over(X,Y):
	over_text=font2.render("GAME OVER",True,(255,255,255))
	screen.blit(over_text,(X,Y))
	
#Score 
def score_disp():
	response1=messagebox.showinfo("Game Over","Your Score is {}".format(str(score_value)))
	sleep(3)
	




running=True
while running:
	
	screen.blit(background,(0,0))


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		
		

	keys = pygame.key.get_pressed()

	if isjump == False:
		if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
			isjump = True
	if isjump:
		F =(1 / 2)*m*(v**2)
		
		dragonY-=0.5*F

		v = v-1
		if v<0:
			m =-1

			
		if v ==-11:
			isjump = False
			v = 10
			m = 1
	
	#Tree Moving and Collision Detection
	for i in range(num_tress):
		treeX[i]-=3.5
		if treeX[i]<0:
			treeX[i]=random.randint(700, 800)
			pygame.time.delay(10)
			#treeX[i]=500
			treeY[i]=348
		tree_obst(treeX[i],treeY[i])
		
		collision=isCollision(treeX[i],treeY[i],dragonX,dragonY)
		if collision:
			
			treeX[i]=0

			game_over(text2X, text2Y)
			running=False
			break

	

	score_value+=1
	show_score(textX, textY)

	dragon_mov(dragonX,dragonY)
	pygame.time.delay(10)
	pygame.display.update()

	

score_disp()

