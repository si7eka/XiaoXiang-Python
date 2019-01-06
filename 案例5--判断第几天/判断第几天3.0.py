"""
知识点：
    集合概念
        集合（set）类型同数字中的集合概念一致，即包含0或多个数据项的无序组合
        集合中的元素不可重复
        集合中的无序组合，没有索引和位置的概念
        set()函数用于集合的生成，返回结果是一个无重复且排序任意的集合
        集合通常用于表示成员间的关系、元素去重等

    集合操作
        设置两个集合 s = {1, 3, 5, 7, 9}   t = {1, 2, 3, 4, 5}
         s - t 或 s.difference(t)        # 返回在集合s中但不在t中的元素，从s中减去t
         s & t 或 s.intersection(t)      # 返回同时在集合s和t中的元素，取交集
         s | t 或 s.union(t)             # 返回集合s和t中的所有元素 ，取并集
         s ^ t 或 s.symmetric_difference(t)   # 返回集合s和t中的元素，但不包含同时在其中的元素，去除相同的元素




作者：si7eklz
版本：1.0
日期：20190101
功能：输入某年某月某日，判断这一天是这一年的第几天
     2.0 新增功能：用列表替换元祖
     3.0 新增功能：使用集合，将月份划分为不同的集合在操作


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
