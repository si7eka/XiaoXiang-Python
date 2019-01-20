"""
知识点：
    面向对象的特点
        封装
            将数据及操作相关打包在一起
            支持代码服用
        继承
            子类（subclass）借用父类（superclass）的行为
            避免重复操作，提升代码服用程度
            定义class ClassName（SuperClassName）
        多态
            在不同情况下用一个函数名启用不用的方法
            灵活性

作者：si7eklz
功能：判断密码强度
日期：20190117
版本：6.0
更新日志：
     4.0 增加功能：从文件中读取密码
     5.0 增加功能：将相关方法封装成一个整体：面向对象编程，定义一个password相关的工具类
     6.0 新增功能：将文件操作封装到一个类中
"""


class PasswordTool:
    """
    密码工具类
    """
    def __init__(self, password):     # 定义一个类 并将外部输入的password传入其中
        # 类的属性
        self.password = password      # 定义类属性
        self.strength_level = 0

    def process_password(self):       # 定义 密码判断过程的方法
        # 规则1 ：密码长度大于8
        if len(self.password) >= 8:     # len判断字符串长度
            self.strength_level += 1
        else:
            print('密码长度至少大于8位')

        # 规则2 ：需要包含数字：
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码至少包含一位数字')

        # 规则3：判断含有字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码至少包含一位字母')

    # 类的方法
    def check_number_exist(self):
        """
            判断密码字符串中是否含有数字
        """
        has_num = False          # 设has_num = False
        for c in self.password:   # 循环遍历password中所有的字符，赋值给c
            if c.isnumeric():    # 如果c是数字
                has_num = True   # 赋值has_num = True
                break            # 终止整个循环
        return has_num           # 输出 has_num

    def check_letter_exist(self):
        """
            判断密码字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        文件作操工具类
    """
    def __init__(self, filepath1):     # 构造函数，或初始化函数
        self.filepath1 = filepath1

    def write_to_file(self, line):
        f = open(self.filepath1, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath1, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
    主函数

    """
    try_times = 5    # 设可以尝试的次数5
    filepath1 = '/Users/monkey/PycharmProjects/XiaoXiang-python/案例6--判断密码强弱/判断密码强弱 6.0/password_6.0.txt'
    # 实例化文件工具对象
    file_tool = FileTool(filepath1)

    while try_times > 0:     # 循环：当尝试次数>0是循环继续

        password = input('请输入密码：')

        # 实例化密码工具对象
        password_tool = PasswordTool(password)     # 将输入的password传入PasswordTool类，并赋值给password_tool
        password_tool.process_password()           # 调用password的方法process_password()

        line = '密码：{}, 强度：{}\n'.format(password, password_tool.strength_level) # 对文件写入password

        # 写操作
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('密码强度合格！')
            break
        else:
            print('密码强度不合格!')
            try_times -= 1
            print()

    if try_times <= 0:
        print('密码设置失败，尝试次数超过5次')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
