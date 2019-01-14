"""
文件基础：
    文件：存储在外部介质（如：硬盘）上的数据或信息的集合
    文本文件：一般指只有字符编码存储的文件，能够被最简单的文本编辑器直接读取
    编码：信息从一种形式转换成另一种形式的过程
    常见编码：
        ASCII,Unicode,UTF-8...
    多行文本，用\n表示换行

文件的操作
    步骤：打开文件 -> 操作文件（读写等）-> 关闭文件

    1. 打开文件：建立文件与程序的连接
    open(filename,mode)
    filename:文件名（包含路径）；mode：打开模式
    打开模式      含义
    r            只读，文件不存在则报错
    w            只写，文件不存在则报错
    a            在文件末尾附加
    r+           读写

    2. 操作文件：写入，读取，等
    写入操作：从计算机内存向文件写入数据
    write()：将文本数据写入文件中
    writelines()：将字符串列表写入文件中

    3. 关闭文件：终止程序与稳健的关联
    close()

作者：si7eklz
功能：判断密码强度
日期：10290109
版本：3.0
     3.0增加功能：保存设置的密码及对应的强度保存到文件中
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

        # 输出密码到txt
        f = open('password_3.0.txt', 'a')  # 不指定绝对路径的话，文件默认是在和程序一个目录中,文件如果不存在则创建  a方法是每次最文件末尾附件 如果w的话会每次覆盖
        f.write('密码：{}, 强度：{}\n' .format(password, strength_level))  # 对文件写入password
        f.close()  # 关闭文件



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