import numpy as np
import matplotlib.pyplot as plt

# 读取图片
im = plt.imread("1.jpg")  # 默认位RGB三通道，R G B 三值相等
img_mat = np.array(im[:, :, 1])  # 取出灰阶矩阵
w, h = img_mat.shape  # 读取图片长和宽

print("original image matrix = \n", img_mat)  # 打印原灰阶图的像素矩阵

titles = ['srcImg', 'bit_plane7', 'bit_plane6', 'bit_plane5', 'bit_plane4', 'bit_plane3', 'bit_plane2', 'bit_plane1',
          'bit_plane0']  # 图片标题
plt.subplot(3, 3, 1)  # 顺序从1开始
plt.imshow(img_mat, cmap='gray')  # 先填进去原图
plt.title(titles[0])

# 位平面切分
for i in range(8):
    # &是位与运算，分别于128、64、32...进行位与，
    # 考虑到低比特位的灰度级太小，展示成图片几乎纯黑，因此* (pow(2, i+1) * (255/256))扩充到[0，255]
    # 注意，img_mat元素为unit8类型，范围为[0,255]，计算过程中为防止越界到256，应先转成int16
    bit_plan_mat = (np.int16(img_mat) & pow(2, 7 - i)) * pow(2, i + 1) * (255 / 256)
    print("bit" + str(7 - i) + " plane = \n", bit_plan_mat)  # 打印每个比特位矩阵
    # 填进各比特位图像和title
    plt.subplot(3, 3, i + 2)
    plt.imshow(bit_plan_mat, cmap='gray')
    plt.title(titles[i + 1])

plt.gcf().set_size_inches(10, 10)  # 设置尺寸
plt.savefig("result.png", dpi=300)  # 保存
plt.show()  # 展示
