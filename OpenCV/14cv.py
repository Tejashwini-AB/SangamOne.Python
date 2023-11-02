import os
info1=os.listdir()

list1=[info1]
list2=[]
print(str(list1))
for photos in info1:
    if photos.endswith('.jpg'):#||.png||.jpeg'
        list2.append(photos)
    elif photos.endswith('.jpeg'):
        list2.append(photos)
    elif photos.endswith('.png'):
        list2.append(photos)

print(list2)


