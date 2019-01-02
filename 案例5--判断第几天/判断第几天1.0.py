"""
需求
输入某年某月某日，判断这一天是这一年的第几天？
例子
    输入日期2017/03/05,是2017年的第几天？
    输入日期2012/03/05,是2012年的第几天？
分析
    1.每个月分的天数不同
    2.闰年与平年的2月份天数不同
    3.闰年判断：（四年一闰and百年不闰） or （四百年再闰）
                (y%4 == 0 and y%100 != 0) or (y%400 == 0)

py功能：
    取余 %
    元组（tuple）
        一旦被创建不能被修改，使得代码更安全
        使用逗号和圆括号来表示，如（2,4,6）
        访问方式和列表相同
        一般用于表达固定数据项，函数多返回值等情况
        特点：
            元素可以为不同类型



    作者：si7eklz
    版本：1.0
    日期：20190101
    功能：输入某年某月某日，判断这一天是这一年的第几天


"""
from datetime import datetime


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期（yyyy/mm/dd）:')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')  #datetime.strptime 字符串转时间类型，input_date_str输入字符串格式
    print(input_date)

    year = input_date.year     # input_date变量中取年
    month = input_date.month   # input_date变量中取月
    day = input_date.day       # input_date变量中取日

    # 计算之前整数月天数和 + 输入的当月天数
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) #平年1-12月每月天数
    # print(days_in_month_tup[: month - 1]) # month - 1 :月份-1 ; days_in_month_tup[: month - 1]:取元祖从开头到月份-1的元素
    days = sum(days_in_month_tup[: month - 1]) + day  # 天数 = 整数月天数和 + 输入的单独天数

    # 判断闰年
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        if month > 2:
            days += 1

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
