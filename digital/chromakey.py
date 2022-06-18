import cv2
import numpy as np

man_image=cv2.imread("man_chromakey.jpg")
ptu_image=cv2.imread("ptu.jpg")

h_m,w_m=man_image.shape[:2]                                 #man_image의 세로(h_m),가로(w_m) 길이
h_p,w_p=ptu_image.shape[:2]                                 #ptu_image의 세로(h_p),가로(w_p) 길이

man_x=400                                                   #man_image를 넣기위한 가로 거리
ptu_roi=ptu_image[h_p-h_m:h_p,man_x:man_x+w_m].copy()       #ptu_image의 세로(h_p)-man_image의 세로(h_m) 즉 man_image가 들어갈 높이 
##이미지 초록색 영역 추출하기
green1=np.array([45,100,100])
green2=np.array([80,255,255])
man_hsv=cv2.cvtColor(man_image,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(man_hsv,green1,green2)
mask_inv=cv2.bitwise_not(mask)


cv2.imshow("mask",mask)
cv2.imshow("mask inv",mask_inv)
cv2.imshow("man",man_image)
cv2.imshow("ptu",ptu_image)
cv2.imshow("roi",ptu_roi)

#클릭 이벤트 함수(위치지정)
def setPosition(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        if x+w_m<=w_p:
            ptu_roi=ptu_image[h_p-h_m:h_p,x:x+w_m].copy()
            cv2.imshow("roi",ptu_roi)
            #이미지에서 초록색제거 후 인물 삽입 부분 제거 
            man_only=cv2.bitwise_and(man_image,man_image,mask=mask_inv)
            background=cv2.bitwise_and(ptu_roi,ptu_roi,mask=mask)
            # cv2.imshow("manOnly",man_only)
            # cv2.imshow("bgd roi",background)
            
            #합성
            new_roi=cv2.add(man_only,background)

            new_image=ptu_image.copy()
            new_image[h_p-h_m:h_p,x:x+w_m]=new_roi
            cv2.imshow("ptu",new_image)

cv2.setMouseCallback("ptu",setPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
