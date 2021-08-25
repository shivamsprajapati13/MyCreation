import pygame

import random 
import math
#Initialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((800,600))

#Background Image
Background=pygame.image.load('background.png')

#Title And Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change=0

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_enemies=6

for i in range(num_enemies):
	enemyImg.append(pygame.image.load('alien.png'))
	enemyX.append(random.randint(0,736))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(5)
	enemyY_change.append(50)

#

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=20
bullet_state="ready"


#Score
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(X,Y):
	score=font.render("Score :"+str(score_value),True,(255,255,255))
	screen.blit(score,(X,Y))

font2=pygame.font.Font('freesansbold.ttf',50)
text2X=400
text2Y=300

def game_over_text(X,Y):
	over_text=font2.render("GAME OVER",True,(255,255,255))
	screen.blit(over_text,(X,Y))

def bullet_fire(X,Y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bulletImg,(X+16,Y+10))
	
def Enemy(X,Y):
	screen.blit(enemyImg[i],(X,Y))

def player(X,Y):
	screen.blit(playerImg,(X,Y))


def isCollosion(enemyX,enemyY,bulletX,bulletY):
	distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
	if distance<27:
		return True
	else:
		return False

#Game Loop
running=True

while running:

	screen.fill((0,0,0))
	screen.blit(Background,(0,0))
		
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN :
			if event.key==pygame.K_LEFT:
				playerX_change=-10
				
			if event.key==pygame.K_RIGHT:
				playerX_change=10

			if event.key==pygame.K_SPACE:
				if bullet_state is "ready":
					bulletX=playerX
					bullet_fire(bulletX,bulletY)

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				playerX_change=0

	playerX+=playerX_change

	if playerX<=0:
		playerX=0
	elif playerX>=768:
		playerX=768

	
	#enemyY+=enemyY_change
	for i in range(num_enemies):
		if enemyY[i]>300:
			for j in range(num_enemies):
				enemyY[j]=2000
			game_over_text(text2X,text2Y)
			break
		enemyX[i]+=enemyX_change[i]

		if enemyX[i]<=0:
			enemyX_change[i]=5
			enemyY[i]+=enemyY_change[i]
			 
		elif enemyX[i]>=736:
			enemyX_change[i]=-5
			enemyY[i]+=enemyY_change[i]

		collosion=isCollosion(enemyX[i],enemyY[i],bulletX,bulletY)

		if collosion:
			bulletY=480 
			bullet_state="ready" 
			score_value+=1 
			
			enemyX[i]=random.randint(0,800)
			enemyY[i]=random.randint(50,150)

				
		Enemy(enemyX[i],enemyY[i])



	#bullet movement
	if bulletY<=0:
		bulletY=480
		bullet_state="ready"
		
	if bullet_state is "fire":
		bullet_fire(bulletX,bulletY)
		bulletY-=bulletY_change

	#Collision 

	


	show_score(textX,textY)
	player(playerX,playerY)
	pygame.display.update()

