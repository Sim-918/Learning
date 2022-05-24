import cv2
import numpy as np

title="MeJot"
image=cv2.imread("messi5.jpg")

h,w=image.shape[:2]
mask=np.zeros((h,w),np.uint8)

cv2.imshow(title,image)
p1x=p1y=0
p2x=p2y=0
def MouseCK(event,x,y,flags,param):
    global p1x,p1y,p2x,p2y
    if event==cv2.EVENT_LBUTTONDOWN:
        p1x,p1y=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        p2x,p2y=x,y
        #사각형 마스크 추출 
        cv2.rectangle(mask,(p1x,p1y),(p2x,p2y),(255,255,255),-1)
        cv2.imshow("mask",mask)
        #사각형 만들기
        cv2.rectangle(image,(p1x,p1y),(p2x,p2y),(0,255,0),0)
        cv2.imshow(title,image)
        #bitwise 마스크 이미지 추출 
        mask_image=cv2.bitwise_and(image,image,mask=mask)
        cv2.imshow("and mask", mask_image)
        #마스크 부분 제거
        mask_inv=cv2.bitwise_not(mask)
        mask_image=cv2.bitwise_and(image,image,mask=mask_inv)
        cv2.imshow("not mask",mask_image)

cv2.setMouseCallback(title,MouseCK)
cv2.waitKey(0)
cv2.destroyAllWindows()
