#Bluring

#평균블러링->cv2.blur(입력이미지,커널크기)
'''
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread('lenna.png')
cv2.imshow("blur",org_image)

def adjustBlur(value):
    if value==0:
        cv2.imshow("blur",org_image)
    else:
        blur_image=cv2.blur(org_image,(value,value))
        cv2.imshow("blur",blur_image)
    
cv2.createTrackbar("K size","blur",3,20,adjustBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#가우시안블러링->cv2.Gaussianblur(입력이미지,커널크기,표준편차)
#바이레터럴->cv2.bilateralFilter(입력이미지,이웃픽셀최대거리,색표준편차,공간표준편차)
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread('lenna.png')
h,w=org_image.shape[:2]

rep_image=cv2.repeat(org_image,1,3)
cv2.imshow("blur",rep_image)

def adjustBlur(value):
    global rep_image,h,w
    if value==0:
        rep_image=cv2.repeat(org_image,1,3)
        cv2.imshow("blur",rep_image)
    else:
        ####원본,평균블러링,가우시간블러링,
        # ksize=2*value+1
        # blur_image=cv2.blur(org_image,(ksize,ksize))
        # rep_image[:,w:2*w]=blur_image
        # gblur_image=cv2.GaussianBlur(org_image,(ksize,ksize),0)
        # rep_image[:,2*w:3*w]=gblur_image
        # cv2.imshow("blur",rep_image)
        ####원본,가우시간블러링,바이래터럴
        sigma=value+10
        gblur_image=cv2.GaussianBlur(org_image,(7,7),0)
        rep_image[:,2*w:3*w]=gblur_image
        cv2.imshow("blur",rep_image)


##가우시간 트랙바
#cv2.createTrackbar("K size","blur",3,10,adjustBlur)
cv2.createTrackbar("sigma","blur",0,140,adjustBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
