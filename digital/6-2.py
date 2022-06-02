###################이미지 크기 변형########################
# import cv2
# import numpy as np

# image=cv2.imread("resize_test.jpg")

# h_m,w_m=image.shape[:2]

# scale=2
# new_size=(w_m*scale,h_m*scale)
# new_image=cv2.resize(image,new_size,interpolation=cv2.INTER_NEAREST)

# cv2.imshow('Original',image)
# cv2.imshow('new Image',new_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
'''
cv2.resize(원래이미지,변형이미지,interpolation=cv2.속성)

'''

'''
정수가 아닐 떄
# scale=2.5
# new_size=(w_m*scale,h_m*scale)
# new_image=cv2.resize(image,new_size,fx=scale,fy=scale,interpolation=cv2.INTER_NEAREST)

'''




###################숫자키 입력받고 크기조정########################
# import cv2
# import numpy as np

# image=cv2.imread("resize_test.jpg")

# h_m,w_m=image.shape[:2]

# scale=1
# while True:
#     new_size=(w_m*scale,h_m*scale)
#     new_image1=cv2.resize(image,new_size,interpolation=cv2.INTER_NEAREST)
#     new_image2=cv2.resize(image,new_size,interpolation=cv2.INTER_LINEAR)

#     cv2.imshow('Original',image)
#     cv2.imshow('Nearest',new_image1)
#     cv2.imshow('Bilinear',new_image2)
#     key=cv2.waitKey(0)
#     if key>=ord('1')and key<=ord('9'):
#         scale=int(chr(key))
#         print(scale)
#     elif key==13:
#         cv2.destroyAllWindows()
#         break
###################축소########################
# import cv2
# import numpy as np

# image=cv2.imread("brick_wall.png")

# h_m,w_m=image.shape[:2]

# scale=0.2
# new_image1=cv2.resize(image,None,fx=scale,fy=scale)
# new_image2=cv2.resize(image,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)

# cv2.imshow('Original',image)
# cv2.imshow('Zoom out1',new_image1)
# cv2.imshow('Zoom out2',new_image2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
###################이미지 회전########################
# import cv2
# import numpy as np

# image=cv2.imread("messi5.jpg")

# h_m,w_m=image.shape[:2]

# scale=0.5
# angle=30
# center=(int(w_m/2),int(h_m/2))

# aff_mat=cv2.getRotationMatrix2D(center,angle,scale)
# new_image=cv2.warpAffine(image,aff_mat,(w_m,h_m))

# cv2.imshow('image',image)
# cv2.imshow('New imaage',new_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
'''
aff_mat=cv2.getRotationMatrix2D(center,angle,scale)
new_image=cv2.warpAffine(image,aff_mat,(w_m,h_m))

'''
###################이미지 회전2########################
# import cv2
# import numpy as np

# image=cv2.imread("messi5.jpg")

# h_m,w_m=image.shape[:2]

# pt_before=[(30,70),(20,240),(300,110)]
# pt_after=[(120,70),(10,180),(280,260)]

# for i in range(len(pt_before)):
#     cv2.circle(image,pt_before[i],3,(0,0,255),-1)

# cv2.imshow('image',image)

# pt_before=np.array(pt_before,np.float32)
# pt_after=np.array(pt_after,np.float32)
# aff_mat=cv2.getAffineTransform(pt_before,pt_after)

# new_image=cv2.warpAffine(image,aff_mat,(w_m,h_m*2))


# cv2.imshow('New imaage',new_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
###################점4개로 찍고 이미지 추출 ########################
import cv2
import numpy as np

image=cv2.imread("ronnie.PNG")
cv2.imshow("Original image",image)

num_pt=0
pt_before=[]
temp_image=image.copy()

def getPoint(event,x,y,flags,param):
    global num_pt,pt_before,temp_image
    if event==cv2.EVENT_LBUTTONDOWN:
        if num_pt!=4:
            pt_before.append((x,y))
            num_pt=num_pt+1
            cv2.circle(temp_image,(x,y),3,(255,255,255),2)
            cv2.imshow("Original image",temp_image)
        else:
            num_pt=0
            temp_image=image.copy()
            cv2.imshow("Original image",temp_image)
            namecarWarp(pt_before)
            pt_before=[]

def namecarWarp(pt1):
    width=((pt1[0][0]-pt1[1][0])**2+(pt1[0][1]-pt1[1][1])**2)**0.5
    width=int(width)
    heigt=int(width*2/3.5)

    pt2=[(0,0),(width,0),(width,heigt),(0,heigt)]
    pt1_m=np.array(pt1,np.float32)
    pt2_m=np.array(pt2,np.float32)

    per_mat=cv2.getPerspectiveTransform(pt1_m,pt2_m)
    new_image=cv2.warpPerspective(image,per_mat,(width,heigt))
    cv2.imshow("New image",new_image)

cv2.setMouseCallback("Original image",getPoint)
cv2.waitKey(0)
cv2.destroyAllWindows()
