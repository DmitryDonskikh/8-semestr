import numpy as np
import cv2
import matplotlib.pyplot as plt

img =cv2.imread("kotik.jpg")
imghsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
th = 150
img1 =imghsv[:,:,2]
msk = img1 > th
msk1 = np.empty(msk.shape, dtype="uint8")
for i in range(msk.shape[0]):
    for j in range(msk.shape[1]):
        if msk[i,j] == True:
            msk1[i,j]=int(1)
        else:
            msk1[i,j]=int(0)
print(msk1)
res = cv2.bitwise_and(img, img, mask=msk1)
plt.imshow(res)
plt.show()