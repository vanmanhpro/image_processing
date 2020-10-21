import cv2 
import numpy as np

# path 
path = 'messi_2_template.jpg'

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# Reading an image in default mode 
src = cv2.imread(path)
  
# Window name in which image is displayed 
window_name = 'Image'
  
# Using cv2.rotate() method 
# Using cv2.ROTATE_180 rotate by  
# 180 degrees clockwise 
image = rotate_image(src, 123)
  
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
