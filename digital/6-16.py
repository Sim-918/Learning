################원본,평균블러링,가우시안블러링,베이레럴필터####################
'''
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("lenna.png")
h,w=org_image.shape[:2]

rep_image=cv2.repeat(org_image,1,3)
cv2.imshow("1",rep_image)

def adjustBlur(value):
    global rep_image,h,w
    if value ==0:
        rep_image=cv2.repeat(org_image,1,3)
        cv2.imshow("1",rep_image)   

    else:
        #원본,평균블러링,가우시안블러링
        # ksize=2*value+1
        # blur_image=cv2.blur(org_image,(ksize,ksize))
        # rep_image[:,w:2*w]=blur_image
        # gblur_image=cv2.GaussianBlur(org_image,(ksize,ksize),0)
        # rep_image[:,2*w:3*w]=gblur_image
        # cv2.imshow("1",rep_image)
        #원본,가우시간블러링,바이래터럴필터
        sigma=value+10
        gblur_image=cv2.GaussianBlur(org_image,(7,7),0)
        rep_image[:,2*w:3*w]=gblur_image
        cv2.imshow("1",rep_image)


# cv2.createTrackbar("k Size","1",0,10,adjustBlur)
    #가우시안 트랙바
cv2.createTrackbar("Sigma","1",0,140,adjustBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
################스레시홀딩####################
# import cv2
# import numpy as np
# import matplotlib.pylab as plt

# org_image=cv2.imread("binarization_2.jpg",cv2.IMREAD_GRAYSCALE)
# h,w=org_image.shape[:2]

# rep_image=cv2.repeat(org_image,1,2)
# cv2.imshow("rep",rep_image)

# def adjustThresh(value):
#     global rep_image,h,w

#     if value ==0:
#         rep_image=cv2.repeat(org_image,1,2)
#         cv2.imshow("rep",rep_image)
#     else:
#         th=value
#         ret_th,bin_image=cv2.threshold(org_image,th,255,cv2.THRESH_BINARY)
#         rep_image[:,0:w]=bin_image
#         #오츠알고리즘이용해 최적의 global threshold 찾기
#         ret_th,bin_image=cv2.threshold(org_image,th,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#         rep_image[:,w:2*w]=bin_image
#         print(ret_th)
#         cv2.imshow("rep",rep_image)

# cv2.createTrackbar("Threashold","rep",0,255,adjustThresh)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
################적응형 이진화####################
'''
import cv2
import numpy as np
import matplotlib.pylab as plt

org_image=cv2.imread("sudoku.png",cv2.IMREAD_GRAYSCALE)
h,w=org_image.shape[:2]

rep_image=cv2.repeat(org_image,1,2)
cv2.imshow("rep",rep_image)

def adjustBlock(value):
    global rep_image,h,w

    if value ==0:
        rep_image=cv2.repeat(org_image,1,2)
        cv2.imshow("rep",rep_image)
    else:   
        block=2*value+1
        rep_th,bin_image=cv2.threshold(org_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        rep_image[:,0:w]=bin_image
        bin_image=cv2.adaptiveThreshold(org_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block,5)

        rep_image[:,w:2*w]=bin_image
        print(rep_th)
        cv2.imshow("rep",rep_image)
        

cv2.createTrackbar("Block Suze","rep",0,50,adjustBlock)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
################경계검출####################
#픽셀값의 큰 변화-> 경계점일 확률이 높다
# import cv2
# import numpy as np
# import matplotlib.pylab as plt

# org_image=cv2.imread("messi5.jpg")
# h,w=org_image.shape[:2]

# org_gray=cv2.cvtColor(org_image,cv2.COLOR_BGR2GRAY)

# y1=100
# cv2.line(org_image,(0,y1),(w,y1),(0,0,255))
# cv2.imshow("org",org_image)

# line1=org_gray[y1,:]
# plt.plot(line1)
# plt.axis([0,w,0,250])
# plt.legend()
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
################sobel filter####################
#수평수직 두자기 필터가 구분됨

# import cv2
# import numpy as np
# import matplotlib.pylab as plt

# org_image=cv2.imread("sudoku.png",cv2.IMREAD_GRAYSCALE)
# cv2.imshow("org",org_image)

# sobel_x=cv2.Sobel(org_image,-1,1,0,3)
# sobel_y=cv2.Sobel(org_image,-1,0,1,3)

# cv2.imshow("sobel_x",sobel_x)
# cv2.imshow("sobel_y",sobel_y)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
################edge세기로 경계 ####################

# import cv2
# import numpy as np
# import matplotlib.pylab as plt

# org_image=cv2.imread("lenna.png",cv2.IMREAD_GRAYSCALE)
# cv2.imshow("org",org_image)

# sobel_x=cv2.Sobel(org_image,-1,1,0,3)
# sobel_y=cv2.Sobel(org_image,-1,0,1,3)

# cv2.imshow("Sobel_x",sobel_x)
# cv2.imshow("Sobel_y",sobel_y)

# sobel_x=sobel_x.astype(np.float32)
# sobel_y=sobel_y.astype(np.float32)

# edge_pow=cv2.magnitude(sobel_x,sobel_y)
# edge_pow=np.clip(edge_pow,0,255)
# edge_pow=edge_pow.astype(np.uint8)

# ret,edge_bin=cv2.threshold(edge_pow,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# edge_bin=cv2.bitwise_not(edge_bin)
# cv2.imshow("Edge",edge_bin)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
##############canny#############
import cv2
from cv2 import Sobel
import numpy as np

org_image=cv2.imread("lenna.png")
cv2.imshow("org",org_image)

org_gray2=cv2.cvtColor(org_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("canny",org_gray2)


th1=50
th2=100
def adjustLow(value):
    global th1,th2
    if value<th2:
        th1=value
    canny_draw(th1,th2)

def adjustHigh(value):
    global th1,th2
    if value>th1:
        th2=value
    canny_draw(th1,th2)

def canny_draw(low_th,high_th):
    canny_image=cv2.Canny(org_gray2,low_th,high_th)

    ret,canny_bin=cv2.threshold(canny_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    canny_bin=cv2.bitwise_not(canny_bin)
    cv2.imshow("canny",canny_bin)



cv2.createTrackbar("Low Treshold","canny",th1,1000,adjustLow)
cv2.createTrackbar("High Treshold","canny",th2,1000,adjustHigh)

cv2.waitKey(0)
cv2.destroyAllWindows()
