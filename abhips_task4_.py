import cv2 as cv
import numpy as np
from math import acos
from math import pi
from math import sqrt
def total(i):
    

    img= cv.imread(i)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresh1=cv.threshold(gray,200,250,0)
    contours1,hierarchy=cv.findContours(thresh1,1,2)
    cnt1= contours1[0]
    M1=cv.moments(cnt1)
    cx1= int(M1['m10']/M1['m00'])
    cy1= int(M1['m01']/M1['m00'])
    l_r=np.array([0,0,220])
    u_r=np.array([10,10,255])
    mask1=cv.inRange(img,l_r,u_r)
    
    ret,thresh2=cv.threshold(mask1,200,250,0)
    contours2,hierarchy=cv.findContours(thresh2,1,2)
    cnt2=contours2[0]
    M2=cv.moments(cnt2)
    cx2= int(M2['m10']/M2['m00'])
    cy2= int(M2['m01']/M2['m00']) 
    l_g=np.array([0,220,0])
    u_g=np.array([10,255,10])
    mask2=cv.inRange(img,l_g,u_g)
    
    ret,thresh3=cv.threshold(mask2,200,250,0)
    contours3,hierarchy=cv.findContours(thresh3,1,2)
    cnt3=contours3[0]
    M3=cv.moments(cnt3)
    cx3= int(M3['m10']/M3['m00'])
    cy3= int(M3['m01']/M3['m00'])
    
    s1=[(cx2-cx1),(cy2-cy1)]
    s2=[(cx3-cx1),(cy3-cy1)]
    cosy=((s1[0]*s2[0])+(s1[1]*s2[1]))/(sqrt(s1[0]**2 + s1[1]**2)*sqrt(s2[0]**2 + s2[1]**2))
    rad=acos(cosy)
    x=(rad*180/pi)
    print(" angle is"+" "+ str(round(x,2))+"degree")
    

total("image_1.png")
total("image_2.png")
total("image_3.png")


cv.waitKey(0)
cv.destroyAllWindows()
    
