import pygame
import random
import time
import os

#Create the screen
window_width = 1200
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))

#Title And Icon
pygame.init()
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()


#Snake Properties
snake_color = (0,255,0)
snake_position = [100,50]

snake_body = [[100, 50],[90, 50],[80, 50],[70, 50]]

direction = 'RIGHT'
change_to = direction
snake_speed = 20


#Food Properties
food_position = [random.randrange(1, (window_width//10)) * 10,random.randrange(1, (window_height//10)) * 10]
food_color = (255,0,0)
food_spawn = True

score = 0


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, (255,0,0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width/2, window_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    os.system("options.py")
    # quit()

running = True
while running:
	# screen.fill((0,255,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
				
			if event.key==pygame.K_LEFT:
				change_to = 'LEFT'
				
			if event.key==pygame.K_UP:
				change_to = 'UP'
				
			if event.key==pygame.K_DOWN:
				change_to = 'DOWN'
				

	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'			

	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	
	snake_body.insert(0, list(snake_position))
	

	if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
		score += 10
		food_spawn = False
	else:
		snake_body.pop()

	if not food_spawn:
		food_position = [random.randrange(1, (window_width//10)) * 10,random.randrange(1, (window_height//10)) * 10]
	food_spawn = True

	screen.fill((205,200,200))


	for i in snake_body:
		pygame.draw.rect(screen, snake_color,pygame.Rect(i[0], i[1], 10, 10))

	pygame.draw.rect(screen,food_color, pygame.Rect(food_position[0], food_position[1], 10, 10))


	if snake_position[0] < 0 or snake_position[0] > window_width-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_height-10:
		game_over()


	# for block in snake_body[1:]:
	# 	if snake_position[0] == block[0] and snake_position[1] == block[1]:
	# 		game_over()

	show_score(1, (255,255,255),'freesansbold.ttf',50)

	pygame.display.update()
	fps.tick(snake_speed)