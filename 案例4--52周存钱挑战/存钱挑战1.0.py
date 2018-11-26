"""
作者：si7eka
功能：52周存钱挑战 10+20+......520=13780
"""

def main():
    """
    主函数
    """
    meizhou_cunru_jine = 10   # 每周存入金额
    i = 1                     # 计数器，记录第几周
    meizhou_dizeng_jine = 10  # 每周递增金额
    yue = 0                   # 余额
    zongzhoushu = 52          # 总周数

    while i <= zongzhoushu:    # while循环 i小于等于总周数时执行下列代码
        # 存钱 yue = yue + meizhou_cunru_jine
        yue += meizhou_cunru_jine

        # 输出余额和周数
        print('第{}周,存入{}元，余额{}'.format(i,meizhou_cunru_jine,yue))    # 使用.format格式化输出

        # 更新下周存钱数额
        meizhou_cunru_jine += meizhou_dizeng_jine
        i += 1


if  __name__ == "__main__":
    main()
