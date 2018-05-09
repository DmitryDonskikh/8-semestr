import cv2
import numpy as np
from PIL import Image
import math

col = [0, 127, 255]
a3 = np.array([[[20, 75], [80, 75], [50, 20]]], dtype=np.int32)


image_1 = np.zeros((100, 100), np.uint8)
image_2 = np.zeros((100, 100), np.uint8)
image_3 = np.zeros((100, 100), np.uint8)

cv2.rectangle(image_1, (20, 20), (80, 80), col[2], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[2], -1)
cv2.fillPoly(image_3, a3, col[2])
fin = np.concatenate((image_1, image_2, image_3), axis = 1)


image_1 = np.zeros((100, 100), np.uint8) + 127
image_2 = np.zeros((100, 100), np.uint8) + 127
image_3 = np.zeros((100, 100), np.uint8) + 127

cv2.rectangle(image_1, (20, 20), (80, 80), col[2], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[2], -1)
cv2.fillPoly(image_3, a3, col[2])
fin2 = np.concatenate((image_1, image_2, image_3), axis = 1)
fin = np.concatenate((fin, fin2), axis = 0)


image_1 = np.zeros((100, 100), np.uint8) + 255
image_2 = np.zeros((100, 100), np.uint8) + 255
image_3 = np.zeros((100, 100), np.uint8) + 255

cv2.rectangle(image_1, (20, 20), (80, 80), col[1], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[1], -1)
cv2.fillPoly(image_3, a3, col[1])
fin2 = np.concatenate((image_1, image_2, image_3),axis = 1)
fin = np.concatenate((fin, fin2), axis = 0)


image_1 = np.zeros((100, 100), np.uint8)
image_2 = np.zeros((100, 100), np.uint8)
image_3 = np.zeros((100, 100), np.uint8)

cv2.rectangle(image_1, (20, 20), (80, 80), col[1], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[1], -1)
cv2.fillPoly(image_3, a3, col[1])
fin2 = np.concatenate((image_1, image_2, image_3), axis = 1)
fin = np.concatenate((fin, fin2), axis = 0)


image_1 = np.zeros((100, 100), np.uint8) + 255
image_2 = np.zeros((100, 100), np.uint8) + 255
image_3 = np.zeros((100, 100), np.uint8) + 255

cv2.rectangle(image_1, (20, 20), (80, 80), col[0], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[0], -1)
cv2.fillPoly(image_3, a3, col[0])
fin2 = np.concatenate((image_1, image_2, image_3), axis = 1)
fin = np.concatenate((fin, fin2), axis = 0)


image_1 = np.zeros((100,100), np.uint8) + 127
image_2 = np.zeros((100,100), np.uint8) + 127
image_3 = np.zeros((100,100), np.uint8) + 127

cv2.rectangle(image_1, (20, 20), (80, 80), col[0], thickness =- 4)
cv2.circle(image_2, (50, 50), 30, col[0], -1)
cv2.fillPoly(image_3, a3, col[0])
fin2 = np.concatenate((image_1, image_2, image_3),axis = 1)
fin = np.concatenate((fin, fin2), axis = 0)
cv2.imshow("final pic", fin)

x,y = np.gradient(fin)

k1 = np.array([[-1/9, -1/9, -1/9], [0, 0, 0], [1/9, 1/9, 1/9]])
x = cv2.filter2D(fin, -1, k1)
k2 = np.array([[-1/9, 0, 1/9], [-3/9, 0, 3/9], [-1/9, 0, 1/9]])
y = cv2.filter2D(fin, -1, k2)

arr1 = np.asarray(x, np.int32)
arr2 = np.asarray(y, np.int32)
for i in range(arr1.__len__()):
    for j in range(arr1[i].__len__()):
        arr1[i, j] = arr1[i, j]/2 + 128
        arr2[i, j] = arr2[i, j]/2 + 128
arr1 = arr1.astype(np.uint8)
arr2 = arr2.astype(np.uint8)
cv2.imshow("ar1", arr1)
cv2.imshow("ar2", arr2)
im1 = Image.fromarray(arr1)
im1.save("arr1.jpeg")
im1 = Image.fromarray(arr2)
im1.save("arr2.jpeg")

finalim = np.zeros((600, 300, 3), np.uint8)
s = np.zeros((600, 300), np.uint8)
for i in range(arr1.__len__()):
     for j in range(arr1[i].__len__()):
        t = math.sqrt(np.int32(arr1[i, j]) ** 2 + np.int32(arr2[i, j]) ** 2)
        s[i, j] = np.uint8(t)
        finalim[i, j, 0] = np.uint8(t)
        finalim[i, j, 1] = arr1[i, j]
        finalim[i, j, 2] = arr2[i, j]
cv2.imshow("123", s)
im1 = Image.fromarray(s)
im1.save("123.jpeg")
cv2.imshow("final", finalim)
im1 = Image.fromarray(finalim)
im1.save("final.jpeg")
cv2.waitKey(0)
