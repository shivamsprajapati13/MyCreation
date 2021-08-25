import imutils
import cv2
import pyautogui

redLower=(157,93,203)
redUpper=(179,255,255)

color = "#000000"
class paintSurface:
    def choose_color(self):
        global color
        color = (colorchooser.askcolor(title ="Choose color")[1])
        
    def paint(self,event):
        currentX1,currentY1 = (event.x-1),(event.y-1)
        currentX2,currentY2 = (event.x+1),(event.y+1)
        cnv.create_line(currentX1, currentY1, currentX2, currentY2, fill = color, capstyle = ROUND, smooth = TRUE, splinesteps = 36, width = 5.0)

camera=cv2.VideoCapture(0)
ps = paintSurface()

while True:
    (grabbed,frame)=camera.read()

    frame=imutils.resize(frame,width=600)
    frame = cv2.flip(frame,1)

    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts) > 0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius > 10 :
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            #print(center,raduis)
            if radius >250:
                       print("stop")
            else:
                
                    if(center[0]<150):
                        cv2.putText(frame, "Left",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
                        print("Left")
                    elif(center[0]>450):
                        cv2.putText(frame, "Right",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
                        print("Right")
                    elif(radius<250):
                        cv2.putText(frame, "Front",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
                        print("Front")
                    else:
                        cv2.putText(frame, "Stop",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
                        print("Stop")

    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
