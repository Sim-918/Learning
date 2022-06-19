#히스토그램 비교
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("mountain.jpg")
org_hsv=cv2.cvtColor(org_image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(org_hsv)

v_e=cv2.equalizeHist(v)
eq_hsv=cv2.merge([h,s,v_e])
eq_image=cv2.cvtColor(eq_hsv,cv2.COLOR_HSV2BGR)

clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
v_c=clahe.apply(v)
clahe_hsv=cv2.merge([h,s,v_c])
clahe_image=cv2.cvtColor(clahe_hsv,cv2.COLOR_HSV2BGR)

cv2.imshow("org",org_image)
cv2.imshow("eql",eq_image)
cv2.imshow("clahe",clahe_image)

org_hist=cv2.calcHist([v],[0],None,[256],[0,255])
eq_hist=cv2.calcHist([v_e],[0],None,[256],[0,255])
clahe_hist=cv2.calcHist([v_c],[0],None,[256],[0,255])

x=np.arange(256)
plt.subplot(3,1,1)
plt.bar(x,org_hist[:,0],label="org")
plt.legend()
plt.subplot(3,1,2)
plt.bar(x,eq_hist[:,0],label="eql")
plt.legend()
plt.subplot(3,1,3)
plt.bar(x,clahe_hist[:,0],label="clahe")
plt.legend()
plt.show()

cv2.destroyAllWindows()
