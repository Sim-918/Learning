#CLAHE객체 생성->cv2.createCLAHE(clipLimit=제한 값,tileGredSize=타일크기)
#CLAHE적용->CLAHE객체.apply(입력이미지)
'''
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("mountain.jpg")
org_hsv=cv2.cvtColor(org_image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(org_hsv)

cv2.imshow("CLAHE",org_image)

def limitChange(value):
    if value==0:
        cv2.imshow("CLAHE",org_image)
    else:
        clahe=cv2.createCLAHE(clipLimit=value,tileGridSize=(8,8))
        v_c=clahe.apply(v)

        clahe_hsv=cv2.merge([h,s,v_c])
        clahe_image=cv2.cvtColor(clahe_hsv,cv2.COLOR_HSV2BGR)
        cv2.imshow("CLAHE",clahe_image)

cv2.createTrackbar("cliplimit","CLAHE",0,10,limitChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
