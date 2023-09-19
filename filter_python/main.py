import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('srcImg.jpg')

# 均值滤波
img_mean3 = cv2.blur(img, (3, 3))
img_mean5 = cv2.blur(img, (5, 5))

# 高斯滤波
img_Guassian3 = cv2.GaussianBlur(img, (3, 3), 0)
img_Guassian5 = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
img_median3 = cv2.medianBlur(img, 3)
img_median5 = cv2.medianBlur(img, 5)

# 展示不同的图片
titles = ['srcImg', 'mean3*3', 'mean5*5', 'Gaussian3*3', 'Gaussian5*5', 'median3*3', 'median5*5']
imgs = [img, img_mean3, img_mean5, img_Guassian3, img_Guassian5, img_median3, img_median5]

for i in range(7):
    plt.subplot(2, 4, i + 1)  # 数组下标从1开始
    plt.imshow(imgs[i])
    plt.title(titles[i])
plt.show()

