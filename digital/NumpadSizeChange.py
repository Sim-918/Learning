#cv2.resize(입력이미지,None,fx=가로변환비율,fy=세로변환비율,interpolation=보간방법)
#cv2.INTER_NEAREST->최근접 이웃보간
#cv2.INTER_LINEAR->양선형 보간
#숫지키로 크기 변경
import cv2
import numpy as np

org_image=cv2.imread("resize_test.jpg")
h_m,w_m=org_image.shape[:2]

scale=1
while True:
    new_size=(w_m*scale,h_m*scale)
    new_image1=cv2.resize(org_image,new_size,interpolation=cv2.INTER_NEAREST)
    new_image2=cv2.resize(org_image,new_size,interpolation=cv2.INTER_LINEAR)

    cv2.imshow("org",org_image)
    cv2.imshow("near",new_image1)
    cv2.imshow("bilinear",new_image2)
    
    key=cv2.waitKey(0)
    if key>=ord('1')and key<=ord('9'):
        scale=int(chr(key))
        print(scale)
    else:
        cv2.destroyAllWindows()
        break
