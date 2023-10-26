import cv2
import numpy as np
img1="p1.jpg"
img2="p2.jpg"
img3="p3.jpg"
img4="p4.jpg"
img5="p5.jpg"
img6="p6.jpg"
img7="p7.jpg"
img8="p8.jpg"
img9="ss.jpg"

bry1=cv2.imread(img1)
bry2=cv2.imread(img2)
bry3=cv2.imread(img3)
bry4=cv2.imread(img4)
bry5=cv2.imread(img5)
bry6=cv2.imread(img6)
bry7=cv2.imread(img7)
bry8=cv2.imread(img8)
bry9=cv2.imread(img9)

r1=np.hori((bry9,bry6,bry5),axis=1)
r2=np.hori((bry7,bry4,bry8),axis=1)
r3=np.hori((bry3,bry2,bry1),axis=1)

matrixcollage=np.verti((r1,r2,r3),axis=0)
cv2.imwrite('matrixcollages.png',matrixcollage)
