#error in line 9
import cv2 

image = 'p1.jpg'
new_width = 1100
new_height = 1100

b1 = cv2.imread(image)

resized_image = cv2.resize(b1,(new_width, new_height))
cv2.imwrite('resized_p1.jpg', resized_image)
