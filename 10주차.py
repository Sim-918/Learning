# ################뒤집기##################
# from turtle import title, width
# import cv2
# import numpy as np

# title='Messi'
# image=cv2.imread("messi5.jpg")

# cv2.imshow(title,image)

# cv2.waitKey(0)

# flip_ud=cv2.flip(image,0)
# cv2.imshow(title,flip_ud)
# cv2.waitKey(0)

# flip_lr=cv2.flip(image,1)
# cv2.imshow(title,flip_lr)
# cv2.waitKey(0)

# flip_both=cv2.flip(image,-1)
# cv2.imshow(title,flip_both)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################반복하기##################
# import cv2
# import numpy as np

# title='Messi'
# image=cv2.imread("messi5.jpg")
# cv2.imshow(title,image)

# cv2.waitKey(0)
# rep_image=cv2.repeat(image,3,2)
# cv2.imshow(title,rep_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################전지정렬##################
# import cv2
# import numpy as np

# title='Messi'
# image=cv2.imread("messi5.jpg")
# cv2.imshow(title,image)

# trans_image=cv2.transpose(image)
# cv2.imshow('trans',trans_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################채널분리'합성##################
# import cv2
# import numpy as np

# title='Messi'
# image=cv2.imread("messi5.jpg")


# h,w,ch=image.shape[:3]
# print(h,w)
# zero=np.zeros((h,w),np.uint8)#정수 8비트
# b,g,r=cv2.split(image)

# cv2.imshow(title,image)
# cv2.waitKey(0)

# new_image=cv2.merge([zero,zero,r])
# cv2.imshow(title,new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################트랙바로 이미지덧셈조정##################
# import cv2
# import numpy as np

# man_face=cv2.imread("man_face.jpg")
# lion_face=cv2.imread("lion_face.jpg")

# alpha=1
# beta=1-alpha
# gamma=0
# man_lion=cv2.addWeighted(lion_face,alpha,man_face,beta,gamma)

# cv2.imshow("man+lion",man_lion)

# def alphaChange(value):
#     global alpha,beta,gamma
#     alpha=value/100
#     beta=1-alpha
#     man_lion=cv2.addWeighted(man_face,alpha,lion_face,beta,gamma)
#     cv2.imshow("man+lion",man_lion)

# cv2.createTrackbar('alpha','man+lion',0,100,alphaChange)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################이미지 마스크와 특정부분추출##################
# from turtle import width
# import cv2
# from cv2 import EVENT_RBUTTONDBLCLK
# import numpy as np

# title='Messi'
# image=cv2.imread("messi5.jpg")

# height,width=image.shape[:2]
# mask=np.zeros((height,width),np.uint8)

# cv2.imshow(title,image)

# pt_x,pt_y=0,0

# def imageMask(event,x,y,flags,param):
#     global pt_x,pt_y
#     if(event==cv2.EVENT_LBUTTONDOWN):
#         pt_x,pt_y=x,y
#     elif(event==cv2.EVENT_LBUTTONUP):
#         cv2.rectangle(mask,(pt_x,pt_y),(x,y),255,-1)
#     elif(event==cv2.EVENT_LBUTTONDBLCLK):
#         cv2.imshow("mask",mask)
#     elif(event==cv2.EVENT_RBUTTONDBLCLK):
#         masked_image=cv2.bitwise_and(image,image,mask=mask)
#         cv2.imshow("Mask image",masked_image)
#     elif(event==cv2.EVENT_MBUTTONDBLCLK):
#         mask_inv=cv2.bitwise_not(mask)
#         masked_image=cv2.bitwise_and(image,image,mask=mask_inv)
#         cv2.imshow("reverse",masked_image)

# cv2.setMouseCallback(title,imageMask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ################이미지 빼기##################
# import cv2
# import numpy as np

# image1=cv2.imread("robot_arm1.jpg")
# image2=cv2.imread("robot_arm2.jpg")
# diff=cv2.absdiff(image1,image2)

# ret,diff=cv2.threshold(diff,10,255,cv2.THRESH_BINARY)
# diff=cv2.bitwise_not(diff)

# cv2.imshow("arm1",image1)
# cv2.imshow("arm2",image2)
# cv2.imshow("diffimg",diff)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

