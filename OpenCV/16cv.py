#def importing():
import os
info1=os.listdir()

list1=[]
list2=[]

list1.append(info1)
print(list1)

for photos in info1:
    if photos.endswith('.jpg'):
        list2.append(photos)
    elif photos.endswith('.jpeg'):
        list2.append(photos)
    elif photos.endswith('.png'):
        list2.append(photos)

print(list2)

file_name='phfile_20230928-_10_01.txt'
with open(file_name,'w')as file:
    for names in list2:
        file.write('%s\n'%names)
