# -*- coding:utf-8 -*-
# 2022/11/29
# Jonathan.K.Wolf
import numpy as np

"""
每一个粒子的形式：
z:
[x, y]
"""
# 种群规模
m = 5
# 迭代参数
c0 = 1
c1 = 2
c2 = 2


# 定义函数
def Rosenbrock(z):
    sum = 100.0 * np.power(z[1] - np.power(z[0], 2), 2) + np.power((1 - z[0]), 2)
    return sum


# 初始化种群
def init_group(size):
    group = []
    for i in range(size):
        group.append([])
    for i in range(size):
        for j in range(2):
            group[i].append(np.random.uniform(-30.0, 30.0))
    return group


# 初始化速度
def init_speed(size):
    speed = []
    for i in range(size):
        speed.append([])
    for i in range(size):
        for j in range(2):
            speed[i].append(np.random.uniform(-60.0, 60.0))
    return speed


# 计算适应度
def calculate_fitness(group):
    fitness = []
    for item in range(len(group)):
        fitness.append(Rosenbrock(group[item]))
    return fitness, fitness.index(min(fitness))


# 更新位置和速度
def update_loc_speed(group, speed, pk, pg):
    new_group = []
    new_speed = []
    for item in range(len(group)):
        new_group.append([])
        new_speed.append([])
    for item in range(len(group)):
        for index in range(len(group[0])):
            new_speed[item].append(
                speed[item][index] + 2 * np.random.rand() * (pk[index] - group[item][index]) + 2 * np.random.rand() * (
                        pg[index] - group[item][index]))
            new_group[item].append(group[item][index] + new_speed[item][index])
    # 限定速度范围
    for item in range(len(speed)):
        for index in range(len(speed[0])):
            if new_speed[item][index] > 60.0:
                new_speed[item][index] = 60.0
            if new_speed[item][index] < -60.0:
                new_speed[item][index] = -60.0
    return new_group, new_speed


# 主要过程迭代
def process():
    epoch = 100000
    group_real = init_group(5)
    speed_real = init_speed(5)
    # 历史最优解
    history_best = group_real[0]
    # 当前最优解
    p = []

    # print(group_real)
    # print(speed_real)
    for i in range(epoch):
        fitness_real, pg_ = calculate_fitness(group_real)
        p.append(group_real[pg_])
        if Rosenbrock(p[i]) <= Rosenbrock(history_best):
            history_best = p[i]
        group_real, speed_real = update_loc_speed(group_real, speed_real, p[i], history_best)
        if i % 100 == 0:
            # print("current epoch:%d, current solution:%e" % (i, Rosenbrock(history_best)))
            print("current epoch:{}, current solution:{}".format(i, history_best))
    print(
        "the answer after {} epoch is ({},{}), and current value is {}".format(epoch, history_best[0], history_best[1],
                                                                               Rosenbrock(history_best)))


if __name__ == '__main__':
    process()
