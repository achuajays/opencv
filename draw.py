import cv2 as cv
import numpy as np
b = np.zeros((500,500,3),dtype='uint8')
cv.imshow('b',b)
b[200:300 , 300:400] = 0,255,3
cv.rectangle(b,(0,0) , (250,250) , (0,255,0) , thickness=2)
cv.imshow('b',b)
img = cv.imread('photo/1.jpg')
cv.imshow('1',img)

cv.waitKey(0)