import os
import numpy as np
import cv2
import imutils

# input folder
infolder = "D:\DDL\images"
# output folder
outfolder = "D:\DDL\images"
for filename in os.listdir(infolder):
    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        
        imgfile = (os.path.join(infolder, filename))
        img = cv2.imread(imgfile, 0)
        startangle = -80
        iteration = 8
        for i in range(iteration):
            outimg = imutils.rotate_bound(img, startangle)
            if startangle <= 0:
                outfile = outfolder + \
                    filename.replace('.JPG', '') + \
                    str(abs(startangle)) + 'L' + ".jpg"
            else:
                outfile = outfolder + \
                    filename.replace('.JPG', '') + \
                    str(startangle) + 'R' + ".jpg"

            wrtstatus = cv2.imwrite(outfile, outimg)
            print(startangle," -- ",outfile, " -- ",wrtstatus )
            startangle = startangle + 20
            if startangle == 0:
                startangle = startangle + 20
            else:
                continue
