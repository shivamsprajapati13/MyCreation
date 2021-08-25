# import cv2
# import imutils

# image=cv2.imread("i1.jpeg")
# image=imutils.resize(image, width=700)
# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# inverted=255-gray_image
# blurred=cv2.GaussianBlur(inverted,(21,21),0)
# invertedblur=255-blurred
# pencilsketch=cv2.divide(gray_image,invertedblur,scale=256.0)
# cv2.imshow("Frame",pencilsketch)




import cv2 as cv
import numpy as np

img=cv.imread('iron.jpg')
#cv.imshow("Image 1",img)


resized_image = cv.resize(img, (500, 500)) 
#cv.imshow("Image 2",resized_image)


gray=cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Image",gray)

blur=cv.GaussianBlur(gray,(7,7),0)
#cv.imshow("Blured Image",blur)

#medblur=cv.medianBlur(gray,0)0
#v.imshow("Blured Image",medblur)

medcanny=cv.Canny(blur,100,200)
cv.imshow("Canny",medcanny)

blurred = cv.bilateralFilter(gray, d=7, sigmaColor=200,sigmaSpace=200)
cv.imshow("burred",blurred)

# bitwise_and=cv.bitwise_and(medcanny,resized_image,mask=None)
# cv.imshow("Color",bitwise_and)

cv.waitKey(0)









#cv2.imwrite("CameraImg.jpg",pencilsketch)

# # import pygame module in this program
# import pygame

# # activate the pygame library .
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()

# # create the display surface object
# # of specific dimension..e(500, 500).
# win = pygame.display.set_mode((500, 500))

# # set the pygame window name
# pygame.display.set_caption("Jump Game")

# # object current co-ordinates
# x = 200
# y = 200

# # dimensions of the object
# width = 30
# height = 40

# # Stores if player is jumping or not
# isjump = False

# # Force (v) up and mass m.
# v = 10
# m = 1

# # Indicates pygame is running
# run = True

# # infinite loop
# while run:

# 	# completely fill the surface object
# 	# with black colour
# 	win.fill((0, 0, 0))

# 	# drawing object on screen which is rectangle here
# 	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	
# 	# iterate over the list of Event objects
# 	# that was returned by pygame.event.get() method.
# 	for event in pygame.event.get():
		
# 		# if event object type is QUIT
# 		# then quitting the pygame
# 		# and program both.
# 		if event.type == pygame.QUIT:
			
# 			# it will make exit the while loop
# 			run = False
# 	# stores keys pressed
# 	keys = pygame.key.get_pressed()
		
# 	if isjump == False:

# 		# if space bar is pressed
# 		if keys[pygame.K_SPACE]:
				
# 			# make isjump equal to True
# 			isjump = True
			
# 	if isjump :
# 		# calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
# 		F =(1 / 2)*m*(v**2)
		
# 		# change in the y co-ordinate
# 		y-= F
		
# 		# decreasing velocity while going up and become negative while coming down
# 		v = v-1
		
# 		# object reached its maximum height
# 		if v<0:
			
# 			# negative sign is added to counter negative velocity
# 			m =-1

# 		# objected reaches its original state
# 		if v ==-11:

# 			# making isjump equal to false
# 			isjump = False

	
# 			# setting original values to v and m
# 			v = 10
# 			m = 1
	
# 	# creates time delay of 10ms
# 	pygame.time.delay(10)

# 	# it refreshes the window
# 	pygame.display.update()
# # closes the pygame window	
# pygame.quit()
