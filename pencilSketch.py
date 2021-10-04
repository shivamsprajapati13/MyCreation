import cv2
import imutils
#Write the Name of the Image here.
image=cv2.imread("i1.jpeg")
image=imutils.resize(image, width=700)
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted=255-gray_image
blurred=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blurred
pencilsketch=cv2.divide(gray_image,invertedblur,scale=256.0)
cv2.imwrite("newImage",pencilsketch)
cv2.imshow("Frame",pencilsketch)



