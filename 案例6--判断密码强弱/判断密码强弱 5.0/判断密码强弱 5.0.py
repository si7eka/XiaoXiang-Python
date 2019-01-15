"""
知识点：
    面向过程vs面向对象



作者：si7eklz
功能：判断密码强度
日期：20190115
版本：5.0
     4.0增加功能：从文件中读取密码
     5.0 增加功能：将相关方法封装成一个整体：面向对象编程，定义一个password相关的工具类
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
        if len(self.password) >= 8:
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


def main():
    """
    主函数

    """
    try_times = 5    # 设可以尝试的次数5

    while try_times > 0:     # 循环：当尝试次数>0是循环继续

        password = input('请输入密码：')

        # 实例化密码工具对象
        password_tool = PasswordTool(password)     # 将输入的password传入PasswordTool类，并赋值给password_tool
        password_tool.process_password()           # 调用password的方法process_password()


        # 输出密码到txt
        f = open('password_5.0.txt', 'a')  # 不指定绝对路径的话，文件默认是在和程序一个目录中,文件如果不存在则创建  a方法是每次最文件末尾附件 如果w的话会每次覆盖
        f.write('密码：{}, 强度：{}\n' .format(password, password_tool.strength_level))  # 对文件写入password
        f.close()  # 关闭文件



        if password_tool.strength_level == 3:
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