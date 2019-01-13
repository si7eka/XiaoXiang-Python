"""
分析：
    如果用户在规定次数内设置符合要求的密码，则终止循环
    如何终止循环？

本次知识点：
    循环终止：
    break语句
        终止整个循环
        例子
        for i in range(100):
            if i % 2 == 0:
                break
            print(i)

    continue语句
        只终止本次循环，而不终止整个循环的执行
        例子
        for i in range(100):
            if i % 2 == 0:
                continue
            print(i)


作者：si7eklz
功能：判断密码强度
日期：10290109
版本：2.0
    2.0增加功能：限制密码设置次数；循环的终止
"""
def check_number_exist(password_str):
    """
        判断密码字符串中是否含有数字
    """
    has_num = False          # 设has_num = False
    for c in password_str:   # 循环遍历password中所有的字符，赋值给c
        if c.isnumeric():    # 如果c是数字
            has_num = True   # 赋值has_num = True
            break            # 终止循环
    return has_num           # 输出 has_num

def check_letter_exist(password_str):
    """
        判断密码字符串中是否含有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
    主函数

    """
    try_times = 5

    while try_times > 0:

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
            break
        else:
            print('密码强度不合格!')
            try_times -= 1
            print()

    if try_times == 0:
        print('密码设置失败，尝试次数超过5次')

if __name__ == '__main__':
    main()