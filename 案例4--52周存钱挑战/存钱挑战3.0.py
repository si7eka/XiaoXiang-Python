"""
作者：si7eka
功能：52周存钱挑战 10+20+......520=13780

使用for x in list:
执行循环 list中的每个元素都会按循环次数被带入x

使用range()创建一个整数列表


"""

import math

def main():
    """
    主函数
    """
    meizhou_cunru_jine = 10   # 每周存入金额
    meizhou_dizeng_jine = 10  # 每周递增金额
    yue_list = []             # 列表型余额

    for i in range(52):
        yue_list.append(meizhou_cunru_jine)    # 使用list.append()将每周存入金额添加到 yue_list中
        yue = math.fsum(yue_list)    # 使用math模块中的math.fsum()计算列表yue_list中所有元素的和

        # 输出余额和周数
        print('第{}周,存入{}元，余额{}'.format(i + 1,meizhou_cunru_jine,yue))    # 使用.format格式化输出

        # 更新下周存钱数额
        meizhou_cunru_jine += meizhou_dizeng_jine
        i += 1


if  __name__ == "__main__":
    main()

