import cv2
import numpy as np
img1="p1.jpg"
img2="p2.jpg"

bry1=cv2.imread(img1)
bry2=cv2.imread(img2)

image1=np.concatenate((bry1,bry2),axis=0)
cv2.imwrite('img1.png',image1)
