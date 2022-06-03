

import cv2
from cv2 import waitKeyEx
from cv2 import waitKey
import numpy as np
import matplotlib.pyplot as plt

IMAGE_H = 700  # 719 Height and 1060 width 
IMAGE_W = 1000

src = np.float32([[120, IMAGE_H], [5500, IMAGE_H], [0, 0], [IMAGE_W, 0]])
dst = np.float32([[400, IMAGE_H], [700, IMAGE_H], [0, 0], [IMAGE_W, 0]])
M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

img = cv2.imread('/home/sushil/Downloads/Bird_eye_view/test2.png') # Read the test img

cv2.imshow("Original image", img)
#cv2.waitKey(0)

img = img[400:(600+IMAGE_H), 0:IMAGE_W] # Apply np slicing for ROI crop
warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H)) # Image warping
plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB)) # Show results
plt.show()