# ################HSV컬러####################
# import cv2 
# import numpy as np

# image=cv2.imread("messi5.jpg")
# hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# hsv_image[:,:,1]=np.clip(hsv_image[:,:,1]*1.5,0,255)
# #hsv_image[:,:,1]=hsv_image[:,:,1]*1.5
# new_image=cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)

# cv2.imshow("messi1",image)
# cv2.imshow("messi2",new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
################채도,명도 변환확인하기####################
# import cv2 
# import numpy as np

# image=cv2.imread("messi5.jpg")
# s_ratio=1
# v_ratio=1

# def satChange(val):
#     global s_ratio,v_ratio
#     s_ratio=val/100
#     hsv_image_update()

# def valChange(val):
#     global s_ratio,v_ratio
#     v_ratio=val/100
#     hsv_image_update()

# def hsv_image_update():
#     global s_ratio,v_ratio
#     hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#     hsv_image[:,:,1]=np.clip(hsv_image[:,:,1]*s_ratio,0,255)#채도
#     hsv_image[:,:,2]=np.clip(hsv_image[:,:,2]*v_ratio,0,255)#명도
#     new_image=cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)
#     cv2.imshow("messi",new_image)

# cv2.imshow("messi",image)

# cv2.createTrackbar('Saturation(%)',"messi",50,200,satChange)#채도 트랙바
# cv2.createTrackbar('Value(%)','messi',50,200,valChange)#명도 트랙바
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################색상의 HSV값 알아내기,추출하기####################
# import cv2 
# import numpy as np

# image=cv2.imread("cube.jpg")
# cv2.imshow("Cube",image)

# def findHSV(event,x,y,flags,param):
#     if event==cv2.EVENT_FLAG_LBUTTON:
#         pixel=np.zeros((1,1,3),np.uint8)
#         pixel[0,0]=image[y,x]
#         print("BRG=",pixel)
#         pixel_hsv=cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV)
#         print("HSV=",pixel_hsv)

#         image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#         low=np.array([pixel_hsv[0,0,0]-2,100,100])
#         high=np.array([pixel_hsv[0,0,0]+2,255,255])
        
#         mask=cv2.inRange(image_hsv,low,high)
#         mask_inv=cv2.bitwise_not(mask)
#         #masked_image=cv2.bitwise_and(image,image,mask=mask)
#         masked_image=cv2.bitwise_and(image,image,mask=mask_inv)
#         #cv2.imshow("Mask",masked_image)
#         cv2.imshow("Mask",mask_inv)
# cv2.setMouseCallback("Cube",findHSV)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################크로마키 합성####################
import cv2 
import numpy as np

man_image=cv2.imread("man_chromakey.jpg")
ptu_image=cv2.imread("ptu.jpg")

h_m,w_m=man_image.shape[:2]
h_p,w_p=ptu_image.shape[:2]

man_x=400
ptu_roi=ptu_image[h_p-h_m:h_p,man_x:man_x+w_m].copy()



# cv2.imshow("Mask",mask)
# cv2.imread("Mask inv",mask_inv)
cv2.imshow("Man",man_image)
cv2.imshow("PTU",ptu_image)
cv2.imshow("PTU ROI",ptu_roi)

green1=np.array([45,100,100])
green2=np.array([80,255,255])
man_hsv=cv2.cvtColor(man_image,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(man_hsv,green1,green2)
mask_ivn=cv2.bitwise_not(mask)
cv2.imshow("Mask",mask)
cv2.imshow("Mask Inv",mask_ivn)

def setPosition(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        if x+w_m<=w_p:
            ptu_roi=ptu_image[h_p-h_m:h_p,x:x+w_m].copy()
            cv2.imshow("PTU ROI",ptu_roi)
            
            man_only=cv2.bitwise_and(man_image,man_image,mask=mask_ivn)
            background=cv2.bitwise_and(ptu_roi,ptu_roi,mask=mask)
            new_roi=cv2.add(man_only,background)

            new_image=ptu_image.copy()
            new_image[h_p-h_m:h_p,x:x+w_m]=new_roi

            cv2.imshow("PTU",new_image)
            
            

cv2.setMouseCallback("PTU",setPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()