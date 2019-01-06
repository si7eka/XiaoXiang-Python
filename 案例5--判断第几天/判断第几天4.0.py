"""
知识点：
    字典概念
        字典类型(dict) 是 "键--值（key -- value）"数据项的组合，每个元素是一个键和值，键是唯一的
            如：身份证号（键）--个人信息（值）
        字典类型数据通过映射查找数据项
        映射：通过任意键查找集合中的值的过程
        字典类型以键为索引，一个键对应一个值
        字典类型的数据是无序的

    字典操作

        key(名称)        value（价格）
        'Eggs'          2.59
        'Milk'          3.19
        'Cheese'        4.80
        'Yogurt'        1.35
        'Butter'        2.59
        'More Cheese'   6.19

        创建字典
            d = dict()
        增加一项
            d[key] = value
        访问
            d[key]
        删除某项
            del d[key]
        key是否在字典中
            key in d




作者：si7eklz
版本：1.0
日期：20190101
功能：输入某年某月某日，判断这一天是这一年的第几天
     2.0 新增功能：用列表替换元祖
     3.0 新增功能：使用集合，将月份划分为不同的集合在操作
     4.0 新增功能：将月份及其对应的天数通过字典表示


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

    # 包含30天 月份集合
    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    # 月份初始天数
    days = 0
    days += day

    for i in range(1, month):         # 遍历从1到month的数字 创建列表赋值给i
        if i in _30_days_month_set:   # 如果i 在_30_days_month_set这个集合中 days赋值30
            days += 30
        if i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
