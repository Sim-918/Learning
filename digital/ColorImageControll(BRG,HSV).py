#칼라 이미지 개선(BRG조작)
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("yacht.jpg")
b,g,r=cv2.split(org_image)

b_e=cv2.equalizeHist(b)
g_e=cv2.equalizeHist(g)
r_e=cv2.equalizeHist(r)

new_image=cv2.merge([b_e,g_e,r_e])
cv2.imshow("org",org_image)
cv2.imshow("equal",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#칼라 이미지 개선(HSV조작)
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("yacht.jpg")
org_hsv=cv2.cvtColor(org_image,cv2.COLOR_BGR2HSV)

h,s,v=cv2.split(org_image)

v_e=cv2.equalizeHist(v)


new_hsv=cv2.merge([h,s,v_e])
new_image=cv2.cvtColor(new_hsv,cv2.COLOR_HSV2BGR)

cv2.imshow("org",org_image)
cv2.imshow("equal",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
