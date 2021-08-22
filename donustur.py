import cv2 as cv 
import numpy as np

img = cv.imread('images/employers.jpg')
cv.imshow('Fotograf', img)

# fotograflarin yerlerini degistirme

def translate(img, x, y):
    donustur = np.float32([[1,0,x],[0,1,y]])
    sekil = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, donustur, sekil)
# -x = sol
# -y yukari
# x = sag
#y sol
donusturulsun = translate(img, 100, 100)
cv.imshow('kaydir', donusturulsun)
# fotografi cevirme

def rotate(img, angle, rotPoint= None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0 ) 
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated =rotate(img,45)
cv.imshow('Rotated', rotated) 
    

cv.waitKey(0)