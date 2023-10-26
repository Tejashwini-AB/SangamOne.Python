import cv2
image1="ju.jpeg"
src1=cv2.imread(image1)
for i in range(1,5,1):
    cv2.imwrite("Planet_"+str(i)+".jpeg",src1)
