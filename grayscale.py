import cv2
import sys
import os
filename = sys.argv[1]
img = cv2.imread( filename ) #input file taken as argument.
img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
cv2.imwrite( "rocket22.png", img ) #Output file.
