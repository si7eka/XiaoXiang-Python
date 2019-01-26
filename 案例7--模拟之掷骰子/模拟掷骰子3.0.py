"""
案例分析：
    Python数据可视化
        matplotlib 模块
            matplotlib 是一个数据可视化函数库
            matplotlib的子模块pyplot提供2D图标制作的基本函数
            例子 https://matplotlib.org/gallery.html

            散点图绘制
            import matplotlib.pyplot as plt  # 导入matplotlib.pyplot模块 别名 plt 
            # x, y分别是x坐标和y坐标的列表
            plt.scatter(x, y)
            plt.show()


作者：si7eklz
功能：模拟掷骰子
版本：3.0
日期：20190126
新增功能：
    3.0 可视化抛掷两个骰子的结果
"""
import random

import matplotlib.pyplot as plt


def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1, 6)   # 生成随机数1-6
    return roll                   # 输出roll


def main():
    """
    主函数
    """
    # 初始化次数
    total_times = 300

    # 初始化列表 [0, 0, 0, 0, 0, 0]，用于记录每次掷骰子的数
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    # 合成字典
    roll_dict = dict(zip(roll_list, result_list))

    # 记录骰子的结果
    roll1_list = []
    roll2_list = []

    # 循环total_times次
    for i in range(total_times):
        # roll 接收roll_dice函数的输出值
        roll1 = roll_dice()
        roll2 = roll_dice()

        # 将两个骰子roll出来的结果添加到roll1_list和roll2_list中
        roll1_list.append(roll1)   
        roll2_list.append(roll2)


        for j in range(2, 13):   # 遍历是2-12的数字
            if (roll1 + roll2) == j:       # 如果 roll1 + roll2 的数字==j
                roll_dict[j] += 1    # 在列表result_dice对应的k的值+1 来记录不通骰子每次得数的次数

    for i, result in roll_dict.items():     # i索引号  result元素值
        print('点数{}的次数：{}，频率：{}'.format(i, result, result / total_times))

    # 数据可视化
    y = range(1, total_times + 1)
    plt.scatter(roll1_list, y, c='Bisque', alpha=0.5)
    plt.scatter(roll2_list, y, c='Coral', alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()
