import cv2
import sys
import os
import numpy as np

#check if there is an image argument and this argument only
if len(sys.argv) != 2:
    print("Usage: python main.py <your_image_name>")
    sys.exit(1)

#check if the file exists
elif not os.path.exists(sys.argv[1]):
    print('File does not exist.\nPlease include your image in the same directory where is main.py file.')
    sys.exit(1)

else:
    #inputing n value until a correct value is inserted
    while 1:
        n = input('Insert value n for matrix dimension 2n+1: ')
        if not n.isnumeric():
            print('Please insert natural number')
        else: break

    dimension = 2*int(n)+1
    blurring_kernel = np.ones((dimension, dimension)) /pow(base=dimension,exp=2)    

    #reading original image from the script argument
    imgArgv = sys.argv[1]
    image = cv2.imread(imgArgv)

    #image convolution with display
    blurred_image = cv2.filter2D(src=image, ddepth=-1, kernel=blurring_kernel)
    cv2.imshow("Blurred Image", blurred_image)

    cv2.waitKey()
    cv2.destroyAllWindows()



