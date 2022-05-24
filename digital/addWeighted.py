import cv2
import numpy as np

# title1='Man'
# title2='Lion'
title3='ManLion'

image1=cv2.imread("man_face.jpg")
image2=cv2.imread("lion_face.jpg")

alpha=0
beta=1-alpha
gamma=0

#알파블렌딩 cv2.addWeighted(이미지1,1의 가중치,이미지2,2의 가중치,추가밝기)
man_lion=cv2.addWeighted(image1,alpha,image2,beta,gamma)

cv2.imshow(title3,man_lion)
# cv2.imshow(title1,image1)
# cv2.imshow(title2,image2)

def TracBar(value):
    global alpha,beta,gamma

    alpha=value/100
    beta=1-alpha
    man_lion=cv2.addWeighted(image1,alpha,image2,beta,gamma)
    cv2.imshow(title3,man_lion)

cv2.createTrackbar("alpha",title3,0,100,TracBar)
cv2.waitKey(0)
cv2.destroyAllWindows()
