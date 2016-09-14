import os
from os import listdir
from os.path import isfile, join
import numpy
import cv2

path1='C:\\Users\\Rohit\\Documents\\MATLAB\\ImageInpaintingCode\\Testdata\\DamagedData'
path2='C:\\Users\\Rohit\\Documents\\MATLAB\\ImageInpaintingCode\\Testdata\\Masks'
damagefiles = [ f for f in listdir(path1) if isfile(join(path1,f)) ]
masks = [ j for j in listdir(path2) if isfile(join(path2,j)) ]

damage_img = numpy.empty(len(damagefiles), dtype=object)
mask_img = numpy.empty(len(masks), dtype=object)

for n in range(0, len(damagefiles)):
  damage_img[n] = cv2.imread( join(path1,damagefiles[n]) )
  mask_img[n] = cv2.imread( join(path2,masks[n]),0 )
  inpaint_img = cv2.inpaint(damage_img[n],mask_img[n],3,cv2.INPAINT_TELEA)
  os.chdir("C:\Users\Rohit\Documents\MATLAB\ImageInpaintingCode\Testdata\ImpaintedImages")
  cv2.imwrite("inpainted_img("+str(n+1)+").jpg",inpaint_img)
  cv2.imshow('Image',inpaint_img)
  cv2.waitKey(1000)
  cv2.destroyAllWindows()
