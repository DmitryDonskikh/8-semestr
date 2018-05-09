import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
mt = np.zeros((1000, 1000, 3), dtype=np.uint8)
for i in range(mt.shape[0]):
    for j in range(mt.shape[1]):
        mt[i, j, 0] = 32 * np.cos(i)
        mt[i, j, 1] = 64 * np.sin(j / 32) + 32
        mt[i, j, 2] = 128 * np.sin((i + j) / 64) + 128
plt.imshow(mt)
plt.show()