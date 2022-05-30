import cv2
import numpy as np

image=cv2.imread("messi5.jpg")
title='MeJot'

s_radio=1
v_radio=1

#채도 함수
def setChange(value):
    global s_radio,v_radio
    s_radio=value/100
    hsv_update()

#밝기 함수
def valChange(value):
    global s_radio,v_radio
    v_radio=value/100
    hsv_update()

def hsv_update():
    global s_radio,v_radio
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_image[:,:,1]=np.clip(hsv_image[:,:,1]*s_radio,0,255)
    hsv_image[:,:,2]=np.clip(hsv_image[:,:,2]*v_radio,0,255)
    new_image=cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)
    cv2.imshow(title,new_image)

cv2.imshow(title,image)
cv2.createTrackbar('Saturation',title,100,200,setChange)
cv2.createTrackbar('Value',title,100,200,valChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
