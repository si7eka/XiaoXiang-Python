"""
文件的操作
    读取操作：从文件中读取数据到计算机内存中
    read()：返回值为包含整个文件内容的的一个字符串
    readline():返回值为文件下一行内容的字符串
    readlines():返回值为整个文件内容的列表，每项是以换行符为结尾的一行字符串

    例子：
    文件的遍历
    f = open('tmp.txt','r')
    for line in f.readlines():
        # 处理一行数据
        pass
    f.close()

    f = open('tmp.txt','r')
    for line in f:
        # 处理一行数据
        pass
    f.close()


作者：si7eklz
功能：判断密码强度
日期：20190114
版本：4.0
     4.0增加功能：从文件中读取密码
"""
def check_number_exist(password_str):
    """
        判断密码字符串中是否含有数字
    """
    has_num = False          # 设has_num = False
    for c in password_str:   # 循环遍历password中所有的字符，赋值给c
        if c.isnumeric():    # 如果c是数字
            has_num = True   # 赋值has_num = True
            break            # 终止整个循环
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
    # try_times = 5
    #
    # while try_times > 0:
    #
    #     password = input('请输入密码：')
    #
    #     # 密码强度
    #     strength_level = 0
    #
    #     # 规则1 ：密码长度大于8
    #     if len(password) >= 8:
    #         strength_level += 1
    #     else:
    #         print('密码长度至少大于8位')
    #
    #     # 规则2 ：需要包含数字：
    #     if check_number_exist(password):
    #         strength_level += 1
    #     else:
    #         print('密码至少包含一位数字')
    #
    #     # 规则3：判断含有字母
    #     if check_letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('密码至少包含一位字母')
    #
    #     # 输出密码到txt
    #     f = open('password_3.0.txt', 'a')  # 不指定绝对路径的话，文件默认是在和程序一个目录中,文件如果不存在则创建  a方法是每次最文件末尾附件 如果w的话会每次覆盖
    #     f.write('密码：{}, 强度：{}\n' .format(password, strength_level))  # 对文件写入password
    #     f.close()  # 关闭文件
    #
    #
    #
    #     if strength_level == 3:
    #         print('密码强度合格！')
    #         break
    #     else:
    #         print('密码强度不合格!')
    #         try_times -= 1
    #         print()
    #
    # if try_times == 0:
    #     print('密码设置失败，尝试次数超过5次')

    #
    #
    # 1. read()
    f = open('password_3.0.txt', 'r')
    read1 = f.read()
    print(read1)
    print('1 end')
    print('')
    print('')
    f.close()

    # 2. readline()
    f = open('password_3.0.txt', 'r')
    line1 = f.readline()
    print(line1)

    line2 = f.readline()
    print(line2)

    print('2 end')
    print('')
    print('')
    f.close()

    # 3-0. readlines()
    f = open('password_3.0.txt', 'r')
    lines = f.readlines()
    print(lines)
    print('3-0 end')
    print('')
    print('')
    f.close()


    # 3-1 遍历
    f = open('password_3.0.txt', 'r')
    for lines31 in f.readlines():
        print('read: {}'.format(lines31))
    print('3-1 end')
    print('')
    print('')

    f.close()

    # 3-2 遍历
    f = open('password_3.0.txt', 'r')
    for lines32 in f:
        print('read:{}'.format(lines32))
    print('3-2 end')
    print('')
    print('')
    f.close()

if __name__ == '__main__':
    main()