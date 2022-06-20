#CLAHE객체 생성->cv2.createCLAHE(clipLimit=제한 값,tileGredSize=타일크기)
#CLAHE적용->CLAHE객체.apply(입력이미지)

import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("before_clahe.PNG")
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

####
import cv2
import numpy as np

ball_image=cv2.imread("golden_earth.jpg")
son_image=cv2.imread("heung_min.jpg")


h_p,w_p=son_image.shape[:2]                                 #son_image의 세로(h_p),가로(w_p) 길이



#이미지축소
scale=0.17
new_ball=cv2.resize(ball_image,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)

h_m,w_m=ball_image.shape[:2]                                 #ball_image의 세로(h_m),가로(w_m) 길이

son_x=550                                                   
son_roi=son_image[h_p-670:h_p,son_x:son_x+220].copy()       #손흥민 공 위치
##이미지 초록색 영역 추출하기(ball 마스크,son마스크)
green1=np.array([45,100,100])
green2=np.array([80,255,255])
#황금공 초록색 영역추출
ball_hsv=cv2.cvtColor(new_ball,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(ball_hsv,green1,green2)
mask_inv=cv2.bitwise_not(mask)
#손흥민 공 초록색 영역 추출
son_hsv=cv2.cvtColor(son_roi,cv2.COLOR_BGR2HSV)
sonmask=cv2.inRange(son_hsv,green1,green2)
sonmaskinv=cv2.bitwise_not(sonmask)


cv2.imshow("ballmask",mask)
cv2.imshow("ballmask inv",mask_inv)
cv2.imshow("ball",new_ball)
cv2.imshow("sonimage",son_image)
cv2.imshow("roi",son_roi)
cv2.imshow("soninv",sonmask)
cv2.imshow("sonball",sonmaskinv)

#클릭 이벤트 함수(위치지정)

def setPosition(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        if x+w_m<=w_p:
            son_roi=son_image[h_p-h_m:h_p,x:x+w_m].copy()
            cv2.imshow("roi",son_roi)
            #이미지에서 초록색제거 후 인물 삽입 부분 제거 
            son_only=cv2.bitwise_and(ball_image,ball_image,mask=mask_inv)
            background=cv2.bitwise_and(son_roi,son_roi,mask=mask)
            # cv2.imshow("manOnly",man_only)
            # cv2.imshow("bgd roi",background)
            
            #합성
            new_roi=cv2.add(son_only,background)

            new_image=son_image.copy()
            new_image[h_p-h_m:h_p,x:x+w_m]=new_roi
            cv2.imshow("sonimage",new_image)
            
cv2.setMouseCallback("sonimage",setPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()

