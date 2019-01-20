"""
案例描述：
    通过计算机程序模拟投掷骰子，并显示各种点数的出现次数及频率
    比如，投掷2个骰子50次，出现点数为7的次数是8，频率是0.16

案例分析：
    如何通过Python模拟随机事件？或者生成随机数？
        random模块
    遍历列表时，如何同时获取每个元素的索引号及其元素值？
        enumerate() 函数
知识点：
    random模块
        用于生成随机数
        常用函数
            函数                  含义
            random()            生成一个[0, 1.0)之间的随机浮点数
            uniform(a, b)       生成一个a到b之间的随机腐恶点数
            randint(a, b)       生成一个a到b之间的随机整数
            choice(<list>)      从列表中随机返回一个元素
            shuffle(<list>)     将列表中元素随机打乱
            sample(<list>, k)  从指定列表中随机获取k个元素
        更多random模块的方法请参考
           https://docs.python.org/3/library/random.html

    enumerate()
        enumerate()函数用于将可遍历的组合转换为一个索引序列
        一般用于for循环中，同时列出元素和元素的索引号

        例子：
        l = ['a', 'b', 'c']
        for x in l:
            print(x)
        输出：
        a
        b
        c

        l = ['a', 'b', 'c']
        for i, x in enumerate(l):
            print('{}--{}'.format(i, x))
        输出：
        0--a
        1--b
        2--c

作者：si7eklz
功能：模拟掷骰子
版本：1.0
日期：20190120
"""
import random


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
    total_times = 1000
    # 初始化列表 [0, 0, 0, 0, 0, 0]，用于记录每次掷骰子的数
    result_list = [0] * 6

    # 循环total_times次
    for i in range(total_times):
        # roll 接收roll_dice函数的输出值
        roll = roll_dice()
        for j in range(1, 7):   # 遍历是1-6的数字
            if roll == j:       # 如果 roll的数字==j
                result_list[j - 1] += 1    # 在列表result_list对应的位置+1 来记录不通骰子每次得数的次数

    for i, result in enumerate(result_list):     # i索引号  result元素值
        print('点数{}的次数：{}，频率：{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
