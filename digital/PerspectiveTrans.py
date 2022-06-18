#원근변환

#원근 변환 행렬 구하기
#cv2.getPerspectiveTranform(변환 전 좌표4개,변환후좌표4개)
#원근변환적용
#cv2.warpPerspective(입력이미지,변환행렬,출력이미지크기)


import cv2
import numpy as np

org_image=cv2.imread("namecard.jpg")
cv2.imshow("org",org_image)

num_pt=0
pt_before=[]
temp_image=org_image.copy()

def getPoints(event,x,y,flags,param):
    global num_pt,pt_before,temp_image
    if event==cv2.EVENT_LBUTTONDOWN:
        if num_pt!=4:
            pt_before.append((x,y))                         #pt_before은 배열형태 그러므로 appen((x,y)) -> [(x,y),(x,y),(x,y)...]                       
            num_pt=num_pt+1
            cv2.circle(temp_image,(x,y),3,(255,0,255),2)
            cv2.imshow("org",temp_image)
        else:
            num_pt=0
            temp_image=org_image.copy()
            cv2.imshow("org",temp_image)
            namecarWarp(pt_before)
            pt_before=[]

#두점사이의 거리공식 이용하기 ((x1-x2)**2+(y1-y2)**2)**0.5
def namecarWarp(ptd1):            
    width=((ptd1[0][0]-ptd1[1][0])**2+(ptd1[0][1]-ptd1[1][1])**2)**0.5
    width=int(width)                                        #integer형으로 변환
    height=int(width*2/3.5)

    ptd2=[(0,0),(width,0),(width,height),(0,height)]
    ptd1_m=np.array(ptd1,np.float32)
    ptd2_m=np.array(ptd2,np.float32)

    per_mat=cv2.getPerspectiveTransform(ptd1_m,ptd2_m)
    new_image=cv2.warpPerspective(org_image,per_mat,(width,height))
    cv2.imshow("new",new_image)

cv2.setMouseCallback("org",getPoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
