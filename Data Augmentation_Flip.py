import os
import numpy as np
import cv2
import imutils
import Augmentor

# input folder
infolder = "D:\DDL\images"
# output folder
outfolder = "D:\DDL\images"
i=0
os.chdir(outfolder)
for filename in os.listdir(infolder):
    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        
        imgfile = (os.path.join(infolder, filename))
        img = cv2.imread(imgfile, 0)
        flip_img1 = cv2.flip(img,0)
        f_name = 'flip_img'+str(i)+'.jpg'
        cv2.imwrite(f_name, flip_img1)
        cv2.imshow("img",flip_img1)
        cv2.waitKey(0)
        print(f_name)
        flip_img2 = cv2.flip(img,1)
        f_name = 'flip_imgg'+str(i)+'.jpg'
        cv2.imwrite(f_name, flip_img2)
        print(f_name)
        i=i+1
        
              
