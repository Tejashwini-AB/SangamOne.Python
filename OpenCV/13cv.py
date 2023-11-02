import os
info1=os.listdir()

list1=[info1]
list2=[]
print(str(list1))
for item in info1:
    if item.endswith('.txt'):
        list2.append(item)

print(list2)
