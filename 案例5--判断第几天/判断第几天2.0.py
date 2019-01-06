"""
知识点：
    列表与元组
        元组是不可变的，列表是可变的
        元组通常由不同的数据组成，列表通常是由相同类型的数据组成
        元组表示的是结构，列表表示的是顺序

    作者：si7eklz
    版本：1.0
    日期：20190101
    功能：输入某年某月某日，判断这一天是这一年的第几天
         2.0 新增功能：用列表替换元祖


"""
from datetime import datetime

def is_leap_year(year):
    """
        判断year是否是闰年
    :param year: 用户输入的年
    :return: 如果是闰年输出True，如果不是闰年输出False
    """
    is_leap = False
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        is_leap = True

    return is_leap

def main():
    """
        主函数
    """
    input_date_str = input('请输入日期（yyyy/mm/dd）:')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')  #datetime.strptime 字符串转时间类型，input_date_str输入字符串格式

    year = input_date.year     # input_date变量中取年
    month = input_date.month   # input_date变量中取月
    day = input_date.day       # input_date变量中取日

    # 计算之前整数月天数和 + 输入的当月天数
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #平年1-12月每月天数
    if is_leap_year(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[: month - 1]) + day  # 天数 = 整数月天数和 + 输入的单独天数

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
