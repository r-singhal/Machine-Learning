#!/usr/bin/env python3

import cv2
import numpy as np

#img=np.zeros([512,512,3])
#print (img)

img=cv2.imread('/home/rishabh/Downloads/superthumb.jpg',1)

newimg=img[200:300,230:430]


#display
#cv2.imwrite('/home/rishabh/Downloads/superthumb.jpg',newimg)

cv2.imshow('imageviewer',newimg)
cv2.waitKey(0)

#to destroy one named window
#cv2.destroyWindows('myownimage')
cv2.destroyWindows('imageviewer')
