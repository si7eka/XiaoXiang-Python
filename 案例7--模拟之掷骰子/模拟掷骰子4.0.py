"""
案例分析：
    Python数据可视化
        matplotlib 模块
            matplotlib 是一个数据可视化函数库
            matplotlib的子模块pyplot提供2D图标制作的基本函数
            例子 https://matplotlib.org/gallery.html

            直方图
            直方图是一种对数据分布情况的图形表示
            首先要对进行分组，然后统计每个分组内数据的数量。
            作用
                显示各分组频率或数量分布的情况
                易于显示各分组之间的频率或数量的差别
        matplotlib 绘制直方图
            import matplotlib.pyplot as plt  # 导入matplotlib.pyplot模块 别名 plt 
            plt.hist(data, bins)
                data 数据
                bins 分组边界

                例子：
                    data = [20, 30, 33, 7, 76 99, 31, 57, 33, 74, 90, 2, 15, 11, 0, 41, 13, 7, 43, 6]
                    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                    plt.hist(data, bins)

作者：si7eklz
功能：模拟掷骰子
版本：4.0
日期：20190126
新增功能：
    4.0 对比结果进行简单的数据统计和分析,使用直方图
"""

import random

import matplotlib.pyplot as plt

# 解决数据可视化中文标题问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换字体
plt.rcParams['axes.unicode_minus'] = False    # 解决符号问题

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

    # 记录骰子的结果
    roll_list = []

    # 循环total_times次
    for i in range(total_times):
        # roll 接收roll_dice函数的输出值
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    # 数据可视化
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1, alpha=0.5)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()
