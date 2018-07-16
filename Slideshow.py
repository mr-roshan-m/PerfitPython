from os import listdir
from os.path import isfile, join
import cv2
folder = "/home/shield/Basics/Python/pics/"
images = [f for f in listdir(folder) if isfile(join(folder, f))] #search for all files and store in array
images.pop(0) #first value in array will be .directory which causes errors.
print(images) #list the final array.
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

for image in images:
	img = cv2.imread(folder+"/"+image)
	# print(img)
	cv2.imshow('image',img)
	cv2.waitKey(0) #waits for keystroke. change to number of seconds to slide automatically.
cv2.destroyAllWindows()