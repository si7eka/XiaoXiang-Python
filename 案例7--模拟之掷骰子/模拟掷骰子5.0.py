"""
知识点
    NumPy(Numeric Python) ：用python实现的科学计算库
    包括：
        1. 强大的N维数组对象array
        2. 成熟的科学函数库
        3. 使用的线性代数，随机数生成函数等
    NumPy的操作对象是多维数组ndarray
        ndarray.shape数组的维度
    创建数组：np.array(<list>), np.arange()......
    改变数组形状reshape()


    NumPy创建随机数组
    np.random.randint(a, b, size)
    创建[a, b)间形状为size的数组
    例如
        import numpy as np
        arr = np.random.randint(1, 10, (3, 4))
        print(arr)

        [[7 8 3 2]
         [7 3 3 2]
         [1 4 3 2]]


NumPy 基本运算
    已数组为对象进行基本运算，即向量化操作
    例如：
         [0 0  0              [0 1 2                   [0 1 2
         10 10 10             0 1 2                    10 11 12 
         20 20 20      +      0 1 2     =              20 21 22
         30 30 30]            0 1 2]                   30 31 32]
    np.histogram()输出直方图的统计结果


作者：si7eklz
功能：模拟掷骰子
版本：5.0
日期：20190126
新增功能：
    5.0 使用科学计算库NUmPy简化程序
"""

import numpy as np

import matplotlib.pyplot as plt

# 解决数据可视化中文标题问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换字体
plt.rcParams['axes.unicode_minus'] = False    # 解决符号问题


def main():
    """
    主函数
    """
    # 初始化次数
    total_times = 300

    # 记录骰子的结果 生成 1-7 total_times的随机数
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(result_arr, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.8)
    
    # 设置x轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', 
                   '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)
    

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()
