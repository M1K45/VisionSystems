import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread('0000021_00000671ms_t1_21_v1_27_t2_29_v2_212.jpg', cv.IMREAD_GRAYSCALE)

# Start point of rectangle contains temperature output only 
x_start_point = 50
y_start_point = 20
# End point of rectangle
x_end_point = 590
y_end_point = 490
 
# Rectangle used for reference only
# cv.rectangle(image,(x_start_point,y_start_point),(x_end_point,y_end_point),(0,255,0),3)

# Cropping for recieving only temperature sensor output
crop = image[y_start_point:y_end_point, x_start_point:x_end_point]

# Image thresholding
_, thresh_bin = cv.threshold(crop, 127, 255, cv.THRESH_BINARY)
_,thresh_otsu = cv.threshold(crop,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
thresh_adaptive = cv.adaptiveThreshold(crop,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,5,2)

cv.imwrite("binary_threshold.jpg", thresh_bin)
cv.imwrite("otsu_threshold.jpg", thresh_otsu)
cv.imwrite("adaptive_threshold.jpg", thresh_adaptive)

cv.waitKey()
cv.destroyAllWindows()