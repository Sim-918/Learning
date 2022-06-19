#덧셈을 통한 밝기 조절
# cv2.add(image,value)
'''
import cv2
import numpy as np

org_image=cv2.imread("lenna.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("lenna",org_image)

def brightUp(value):
    temp_image=cv2.add(org_image,value)
    cv2.imshow("lenna",temp_image)

def brightDown(value):
    temp_image=cv2.add(org_image,-value)
    cv2.imshow("lenna",temp_image)

cv2.createTrackbar("up","lenna",0,255,brightUp)
cv2.createTrackbar("down","lenna",0,255,brightDown)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#곱셈을 통한 밝기 조절
#cv2.multiply(iamge,scale)
'''
import cv2
import numpy as np

org_image=cv2.imread("lenna.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("lenna",org_image)

def brigtChange(value):
    scale=value/100
    temp_image=cv2.multiply(org_image,scale)
    cv2.imshow("lenna",temp_image)

cv2.createTrackbar("chage(%)","lenna",100,200,brigtChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#효과적인 명암비 조절
'''
import cv2
import numpy as np

org_image=cv2.imread("lenna.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("lenna",org_image)

def contrastChange(value):
    scale=(value-100)/100
    print(scale)
    temp_image=org_image.astype(np.float32)
    temp_image=temp_image+(temp_image-128)*scale
    temp_image=np.clip(temp_image,0,255)
    temp_image=temp_image.astype(np.uint8)
    cv2.imshow("lenna",temp_image)


cv2.createTrackbar("Constrast","lenna",100,200,contrastChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
