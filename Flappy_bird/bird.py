import pygame
import pyautogui
import random 
import math
from time import sleep
import os

#Initialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((400,500))

#Background Image
Background=pygame.image.load('background.png')

#Title And Icon
pygame.display.set_caption("Flappy Bird")

#Pipes
pipe1 = []
pipe1X = []
pipe1Y = []

pipe2 = []
pipe2X = []
pipe2Y = []

pipe_num = 5

for i in range(pipe_num):
	pipe1.append(pygame.image.load('pipe_down.png'))
	pipe2.append(pygame.image.load('pipe_up.png'))
	pipe1X.append(400)
	pipe1Y.append(350)

	pipe2X.append(400)
	pipe2Y.append(-80)

def pipes(X,Y):
	screen.blit(pipe1[i],(X,Y))
	screen.blit(pipe2[i],(X,Y)) 

	# screen.blit(pipe_img_up,(X,Y))


bird_img = pygame.image.load('bird.png')
bird_imgX = 30
bird_imgY = 200
bird_imgX_change = 0

def bird(X,Y):
	screen.blit(bird_img,(X,Y))


def collision(bird_imgX,bird_imgY,pipe1X,pipe1Y,pipe2X,pipe2Y):
	distance1 = math.sqrt((math.pow(bird_imgX-pipe1X,2))+(math.pow(bird_imgY-pipe1Y,2)))
	distance2 = math.sqrt((math.pow(bird_imgX-pipe2X,2))+(math.pow(bird_imgY-pipe2Y,2)))
	
	
	if distance1 < 20:
		print("collision1")
		return True
		#print(distance1)

	if distance2 < 310:

		print("collison2 \n ",distance2)
		return True
		print(distance2)

def game_over():
	os.system('game_over.py')



running = True
while running:
	# mouseX,mouseY = pyautogui.position()
	# print(mouseX,mouseY)

	screen.fill((0,0,0))
	screen.blit(Background,(0,0))

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

		if event.type==pygame.KEYDOWN :
			if event.key==pygame.K_UP:
				bird_imgY-=50



	if bird_imgY >500:
		bird_imgY = 0


	for i in range(pipe_num):
		pipe1X[i]-=0.5
		pipe2X[i]-=0.5

		if (pipe1X[i] and pipe2X[i]) < 0:
			pipe1X[i] = 400
			pipe1Y[i] = 350
			pipe2X[i] = 400
			pipe2Y[i] = -80
		
		iscollision = collision(bird_imgX,bird_imgY,pipe1X[i],pipe1Y[i],pipe2X[i],pipe2Y[i])
		# sleep(10)
		# if iscollision:
			# running = False
			# game_over()

			


		pipes(pipe1X[i],pipe1Y[i])
		pipes(pipe2X[i],pipe2Y[i])


	bird_imgY+= 0.2

	bird(bird_imgX, bird_imgY)

	pygame.display.update()