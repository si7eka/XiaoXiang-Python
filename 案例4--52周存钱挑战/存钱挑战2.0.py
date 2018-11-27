"""
作者：si7eka
功能：52周存钱挑战 10+20+......520=13780

Python列表函数&方法
http://www.runoob.com/python3/python3-list.html
http://www.runoob.com/python/python-lists.html

math模块
https://docs.python.org/3/library/math.html?highlight=math#module-math
"""

import math

def main():
    """
    主函数
    """
    meizhou_cunru_jine = 10   # 每周存入金额
    i = 1                     # 计数器，记录第几周
    meizhou_dizeng_jine = 10  # 每周递增金额
    zongzhoushu = 52          # 总周数
    # yue = 0  # 余额
    yue_list = []             # 列表型余额

    while i <= zongzhoushu:    # while1列代码
        yue_list.append(meizhou_cunru_jine)    # 使用list.append()将每周存入金额添加到 yue_list中
        yue = math.fsum(yue_list)    # 使用math模块中的math.fsum()计算列表yue_list中所有元素的和

        # 输出余额和周数
        print('第{}周,存入{}元，余额{}'.format(i,meizhou_cunru_jine,yue))    # 使用.format格式化输出

        # 更新下周存钱数额
        meizhou_cunru_jine += meizhou_dizeng_jine
        i += 1


if  __name__ == "__main__":
    main()

