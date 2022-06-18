# #어파인 변환 적용(이미지 회전)
# #cv2.warpAffine(입력이미지,어파인행렬,출력이미지크기)
# import cv2
# import numpy as np

# org_image=cv2.imread("messi5.jpg")
# h_m,w_m=org_image.shape[:2]

# center=(int(w_m/2),int(h_m/2))
# angle=30
# scale=0.5

# aff_mat=cv2.getRotationMatrix2D(center,angle,scale)
# new_image=cv2.warpAffine(org_image,aff_mat,(w_m,h_m))

# cv2.imshow("Org",org_image)
# cv2.imshow("new",new_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


########지정한좌표로 회전########
import cv2
import numpy as np

org_image=cv2.imread("messi5.jpg")

h_m,w_m=org_image.shape[:2]

pt_before=[(30,70),(20,240),(300,100)]
pt_after=[(120,20),(10,180),(280,260)]

for i in range(len(pt_before)):
    cv2.circle(org_image,pt_before[i],3,(0,0,255),-1)       #pt_before좌표에 점을 찍음

cv2.imshow("org",org_image)


#좌표 3개를 np 행렬로 표현
pt_before=np.array(pt_before,np.float32)
pt_after=np.array(pt_after,np.float32)
aff_mat=cv2.getAffineTransform(pt_before,pt_after)

new_image=cv2.warpAffine(org_image,aff_mat,(w_m,h_m*2))
cv2.imshow("new",new_image)



cv2.waitKey(0)
cv2.destroyAllWindows()
