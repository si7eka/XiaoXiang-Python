"""
案例描述：
    通过计算机程序模拟投掷骰子，并显示各种点数的出现次数及频率
    比如，投掷2个骰子50次，出现点数为7的次数是8，频率是0.16

案例分析：
    如何通过Python模拟随机事件？或者生成随机数？
        random模块
    遍历列表时，如何同时获取每个元素的索引号及其元素值？
        enumerate() 函数
    如何将对应的点数和次数关联起来？
        zip()函数
知识点：
    zip()函数用于将对应的元素打包成一个个元组

    l1 = [1, 2, 3, 4, 5]
    l2 = ['a', 'b', 'c', 'd', 'e']
    zip(l1, l2)
    注意：元组中的元素是不可修改的，若要修改需要转成字典或其他
    dict(zip(l1, l2))
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


作者：si7eklz
功能：模拟掷骰子
版本：2.0
日期：20190123
新增功能：
    2.0 模拟两个骰子
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
    total_times = 10000

    # 初始化列表 [0, 0, 0, 0, 0, 0]，用于记录每次掷骰子的数
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))

    # 合成字典
    roll_dict = dict(zip(roll_list, result_list))



    # 循环total_times次
    for i in range(total_times):
        # roll 接收roll_dice函数的输出值
        roll1 = roll_dice()
        roll2 = roll_dice()
        for j in range(2, 13):   # 遍历是2-12的数字
            if (roll1 + roll2) == j:       # 如果 roll1 + roll2 的数字==j
                roll_dict[j] += 1    # 在列表result_dice对应的k的值+1 来记录不通骰子每次得数的次数

    for i, result in roll_dict.items():     # i索引号  result元素值
        print('点数{}的次数：{}，频率：{}'.format(i, result, result / total_times))


if __name__ == '__main__':
    main()
