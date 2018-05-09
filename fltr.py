import cv2
import numpy as np
from matplotlib import pyplot as plt

image =cv2.imread("kotik.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_in_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(image_in_gray, cmap="gray")
plt.show()
kernel = np.array([-0.5, 0.5])
dst = cv2.filter2D(image_in_gray,-1,kernel)
plt.imshow(dst,cmap="gray")
plt.show()
print(kernel)