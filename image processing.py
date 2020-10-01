import numpy as np
import cv2 as cv
img1=  cv.imread("image1.jpg")
img2 = cv.imread("image2.png")
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,thresh1=cv.threshold(gray1,200,255,0)
ret,thresh2=cv.threshold(gray2,200,255,0)
contours1,hierarchy=cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours2,hierarchy=cv.findContours(thresh2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

def A():
    print ("rows,columns and channels")
    img1=  cv.imread("image1.jpg")
    img2 = cv.imread("image2.png")
    print ("image1:")
    print( img1.shape )
    print( 'image2:')
    print( img2.shape)
    cv.waitKey(0)
    cv.destroyAllWindows()

A()

def B():
    print("intensity of image(red,green and blue)")
    print("image1")
    px1=img1[100,100,(2,1,0)]
    print (px1)
    print("image2")
    px2=img2[100,100,(2,1,0)]
    print(px2)
B()

def C ():
    gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY) 
    ret, thresh1 = cv.threshold(gray1, 200, 255, 0)
    contours1, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img1, contours1,-1, (0,255,0), 3)
    print ("image1")
    for i in range(len(contours1)):
        print ("area"+str(i+1)+ ":",cv.contourArea(contours1[i]) )
        print ("perimeter"+str(i+1)+":",cv.arcLength(contours1[i],True))
    cv.imshow("image",img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)   
    ret, thresh2 = cv.threshold(gray2,200, 255, 0)
    contours2, hierarchy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img2, contours2, -1, (0,255,0), 3)

    print ("image2")

    for i in range(len(contours2)):
        
        print ("area"+str(i+1)+ ":",cv.contourArea(contours2[i]) )

        print ("perimeter"+str(i+1)+":",cv.arcLength(contours2[i],True))

    cv.imshow("image",img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
C()
def D ():
    area1=[]
    for i in range(1,len(contours1)):
           x=cv.contourArea(contours1[i])
           area1.append(x)
        
    print("maximum area=",max(area1))
    m=int(area1.index(max(area1)))
    print("and perimeter=",cv.arcLength(contours1[m+1],True))
    cv.drawContours(img1,contours1,m+1,(0,255,0),3)
    cv.imshow("image1",img1)

    area2=[]
    for i in range(1,len(contours2)):
           x=cv.contourArea(contours2[i])
           area2.append(x)
        
    print("maximum area=",max(area2))
    m=int(area2.index(max(area2)))
    print("and perimeter=",cv.arcLength(contours2[m+1],True))
    cv.drawContours(img2,contours2,m+1,(0,255,0),3)
    cv.imshow("image2",img2)
D()

def E ():
    gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
    gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
    cv.imshow("image1",gray1)
    cv.imshow("image2",gray2)

E()

def F():
    r1=img1.copy()
    r2=img2.copy()
    r1[:,:,0]=0
    r1[:,:,1]=0
    r2[:,:,0]=0
    r2[:,:,1]=0
    cv.imshow("image1",r1)
    cv.imshow("image2",r2)
F()


















