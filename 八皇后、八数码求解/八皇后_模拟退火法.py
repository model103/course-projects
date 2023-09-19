import numpy as np
import random
import time
import math


# 模拟退火算法解决八皇后问题
# 八皇后初始化函数
def init():
    cache = {}
    m = np.zeros((8, 8), dtype=int)
    for i in range(0, 8):
        temp = random.randrange(0, 8)
        m[temp, i] = 1
        cache["queen" + str(i)] = [temp, i]
    return m, cache


# 计算当前状态无碰撞数量
def compute_weight_single(coord_cache):
    weight = 0
    for i in range(0, 8):
        x, y = coord_cache["queen" + str(i)]
        for j in range(i + 1, 8):
            _x, _y = coord_cache["queen" + str(j)]
            if _x - x == j - i or _x - x == i - j:
                weight += 1
            if _x == x:
                weight += 1
    return 28 - weight


# 随机生成一个新的解
def random_adjust(coord_cache):
    # fix_bug 这里传入的字典必须使用deepcopy
    temp = copy.deepcopy(coord_cache)
    row = random.randrange(0, 8)
    column = random.randrange(0, 8)
    temp["queen" + str(column)] = [row, column]  # 调整皇后的位置
    return temp


# 把当前的皇后状态画出来
def draw(coord_cache):
    m = np.zeros((8, 8), dtype=int)
    for i in range(8):
        row, column = coord_cache["queen" + str(i)]
        row, column = int(row), int(column)
        m[row][column] = 1
    return m


# 模拟退火算法
def sa_algorithm(temperature, temperature_min, r, L):
    """
    :param temperature: 初始温度值
    :param r:用于控制降温的快慢
    :param temperature_min:温度下限，低于这个温度还没有找到最优解算法结束
    :param L:每个温度的迭代次数
    :return:null
    """
    m, coord_cache = init()
    print("初始化八皇后状态为：\n", m)
    while temperature > temperature_min:  # 温度循环
        for i in range(L):  # 每个温度循环L次
            weight = compute_weight_single(coord_cache)
            print("当前状态的无碰撞度为：", weight)
            if weight == 28:  # 非碰撞度为28，表明找到了最优解
                return True
            new_coord_cache = random_adjust(coord_cache)  # 随机调整得到一个新的解
            new_weight = compute_weight_single(new_coord_cache)  # 计算新解的碰撞度
            print("随机调整产生的新解为：\n", draw(new_coord_cache))
            print("随机调整产生的新解的无碰撞度为：", new_weight)
            if new_weight >= weight:  # 新的解碰撞度更小就就收这个解
                coord_cache = new_coord_cache
                print("这是一个更好的解，直接接收：\n", draw(coord_cache))
            else:
                if random.random() < math.exp((new_weight - weight) / temperature):  # 否则就已模拟退火的概率接受作为新的解
                    coord_cache = new_coord_cache
                    print("当前的接收概率为：", math.exp((new_weight - weight) / temperature))
                    print("这是一个更差的解，但被接收了：\n", draw(coord_cache))

        temperature = temperature * r


def SA_algorithm_test(temperature, temperature_min, r, L, num):
    tic = time.time()
    success_case = 0
    fail_case = 0
    for i in range(num):
        if sa_algorithm(temperature, temperature_min, r, L):
            success_case += 1
            print("第{0}个例子找到了最优解".format(i))
        else:
            fail_case += 1
            print("第{0}个例子失败".format(i))
    toc = time.time()
    print("{0}个例子中成功解决的例子为：{1}".format(num, success_case))
    print("{0}个例子成功解决的百分比为：{1}".format(num, success_case / num))
    print("{0}个例子中失败的例子为：{1}".format(num, fail_case))
    print("{0}个例子失败的百分比为：{1}".format(num, fail_case / num))
    print("{0}个例子运行算法所需的时间为：{1}秒".format(num, toc - tic))


SA_algorithm_test(temperature=5, temperature_min=0.001, r=0.98, L=150, num=1000)