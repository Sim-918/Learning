import cv2
import numpy as np

image=cv2.imread("cube.jpg")
title='cube'
cv2.namedWindow(title,cv2.WINDOW_NORMAL)
cv2.imshow(title,image)

def findHSV(event,x,y,flasg,param):
    if event==cv2.EVENT_LBUTTONDOWN:
            pixel=np.zeros((1,1,3),np.uint8)    
            pixel[0,0]=image[y,x]
            print("BRG=",pixel)
            pixel_hsv=cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV)
            print("HSV=",pixel_hsv)

            image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            low=np.array([pixel_hsv[0,0,0]-2,100,100])
            high=np.array([pixel_hsv[0,0,0]+2,255,255])
            #마스크 추출
            mask=cv2.inRange(image_hsv,low,high)
            cv2.imshow("MAsk",mask)
            #특정 마스크 출력
            mask_image=cv2.bitwise_and(image,image,mask=mask)
            cv2.imshow("mask color",mask_image)
            
    

cv2.setMouseCallback(title,findHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()
