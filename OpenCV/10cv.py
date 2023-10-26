import cv2
def imjoin2(fname2):
    
    def imjoin1(n1,n2,n3,n4,n5,n6,n7,n8,n9):
        
        img1=n1
        img2=n2
        img3=n3
        img4=n4
        img5=n5
        img6=n6
        img7=n7
        img8=n8
        img9=n9

        bry1=cv2.imread(img1)
        bry2=cv2.imread(img2)
        bry3=cv2.imread(img3)
        bry4=cv2.imread(img4)
        bry5=cv2.imread(img5)
        bry6=cv2.imread(img6)
        bry7=cv2.imread(img7)
        bry8=cv2.imread(img8)
        bry9=cv2.imread(img9)

        r1=cv2.hconcat((bry9,bry6,bry5))
        r2=cv2.hconcat((bry7,bry4,bry8))
        r3=cv2.hconcat((bry3,bry2,bry1))

        matrixcollage=cv2.vconcat((r1,r2,r3))
        cv2.imwrite('matrix_collages_20230928_4.png',matrixcollage)
    f1=open(fname2,'r')
    im1=f1.readline().replace('\n','')
    im2=f1.readline().replace('\n','')
    im3=f1.readline().replace('\n','')
    im4=f1.readline().replace('\n','')
    im5=f1.readline().replace('\n','')
    im6=f1.readline().replace('\n','')
    im7=f1.readline().replace('\n','')
    im8=f1.readline().replace('\n','')
    im9=f1.readline().replace('\n','')
    imjoin1(im1,im2,im3,im4,im5,im6,im7,im8,im9)
imjoin2('fnames.txt')
