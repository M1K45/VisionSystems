import cv2

img = cv2.imread('mariusz.jpg') 
cv2.rectangle(img,(384,15),(510,128),(0,255,0),3)
cv2.circle(img,(200, 100), 63, (0,0,255), 3)
cv2.ellipse(img,(256,256),(100,50),0,0,360,(0,255,255),3)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.jpg', img)