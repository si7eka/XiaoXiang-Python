"""
作者：si7eka
功能：52周存钱挑战 10+20+......520=13780
版本：5.0

使用for x in list:
执行循环 list中的每个元素都会按循环次数被带入x

使用range()创建一个整数列表
"""

import math


def cun_qian_n_zhou(meizhou_cunru_jine,meizhou_dizeng_jine,zongzhoushu):
    """
        存钱计算函数`
    :param meizhou_cunru_jine: 每周存入金额
    :param meizhou_dizeng_jine: 每周递增金40-3额
    :param zongzhoushu: 总周数
    """

    yue_list = []  # 列表型余额，每周存款数量
    saved_money_lisy = [] # 记录每周账户累计


    for i in range(zongzhoushu):
        yue_list.append(meizhou_cunru_jine)  # 使用list.append()将每周存入金额添加到 yue_list中
        yue = math.fsum(yue_list)  # 使用math模块中的math.fsum()计算列表yue_list中所有元素的和
        saved_money_lisy_list.append(yue)

        # 输出余额和周数
        print('第{}周,存入{}元，余额{}'.format(i + 1, meizhou_cunru_jine, yue))  # 使用.format格式化输出

        # 更新下周存钱数额
        meizhou_cunru_jine += meizhou_dizeng_jine
        i += 1

    return(saved_money_lisy)

def main():
    """
        主函数
    """
    meizhou_cunru_jine = float(input('输入每周存入金额：'))   # 每周存入金额
    meizhou_dizeng_jine = float(input('输入每周递增金额：'))  # 每周递增金额
    zongzhoushu = int(input('总周数：'))                     # 总周数


    # 调用存钱函数
    cun_qian_n_zhou(meizhou_cunru_jine,meizhou_dizeng_jine,zongzhoushu)

if  __name__ == "__main__":
    main()


