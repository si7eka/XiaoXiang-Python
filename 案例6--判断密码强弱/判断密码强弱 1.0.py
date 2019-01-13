"""
密码规则：
    密码长度至少8位
    密码含有数字
    密码含有字母

分析：
    先设置一个密码强度的变量初始值为0，满足一个规则 自+1 当等于3的时候即为强密码
    长度判断L使用len()方法
    包含数字判断：使用isnumeric()方法
    包含字母判断：使用isalpha()方法
    如果strength_level等于3，密码强度合格，否则不合格

本次知识点：
    Python字符串操作
        str.isnumeric()
        检测字符串是否只由数字组成
        str.isalpha()
        检测字符串是否只由字母组成
        str.islower()
        检测字符串中所有的字母是否都是小写
        str.isupper()
        检测字符串所有字母是否都为大写
        更多isxxxx()方法请参考
        https://docs.python.org/3/library/stdtypes.html#string-methods


作者：si7eklz
功能：判断密码强度
日期：10290109
"""
def check_number_exist(password_str):
    """
        判断密码字符串中是否含有数字
    """
    for c in password_str:   # 循环遍历password中所有的字符，赋值给c
        if c.isnumeric():    # 如果c是数字
            return True      # 输出True
    return False             #

def check_letter_exist(password_str):
    """
        判断密码字符串中是否含有字母
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
    主函数

    """
    password = input('请输入密码：')

    # 密码强度
    strength_level = 0

    # 规则1 ：密码长度大于8
    if len(password) >= 8:
        strength_level += 1
    else:
        print('密码长度至少大于8位')

    # 规则2 ：需要包含数字：
    if check_number_exist(password):
        strength_level += 1
    else:
        print('密码至少包含一位数字')

    # 规则3：判断含有字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('密码至少包含一位字母')

    if strength_level == 3:
        print('密码强度合格！')
    else:
        print('密码强度不合格!')


if __name__ == '__main__':
    main()