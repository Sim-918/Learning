#cv2.resize(입력이미지,None,fx=가로변환비율,fy=세로변환비율,interpolation=보간방법)
#cv2.INTER_NEAREST->최근접 이웃보간
#크기변형
import cv2
import numpy as np

org_image=cv2.imread("resize_test.jpg")
h_m,w_m=org_image.shape[:2]

scale=2
new_size=(w_m*scale,h_m*scale)
new_image=cv2.resize(org_image,new_size,interpolation=cv2.INTER_NEAREST)
'''
정수형이 아닐경우
scale=2.5
new_size=(w_m*scale,h_m*scale)
new_image=cv2.resize(org_image,None,fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST)
'''
cv2.imshow("org",org_image)
cv2.imshow("resize",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
