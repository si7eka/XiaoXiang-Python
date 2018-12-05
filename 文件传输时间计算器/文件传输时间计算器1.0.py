"""
作者：si7eka
功能：文件传输时间计算器

计算所述文件传输时间（t），文件大小（fs）和传输速度（ts）的关系。不考虑网络延迟和数据包数据丢失，结果仅供参考。

文件大小 (fs)
  MB
传输速度 (ts)
  Mbit/s
时间  (time) = 8.s

"""


def main():
    """
    主函数
    """
    yes_or_no = input('输入任意键继续，退出请输入no。')

    while yes_or_no != "no":
        print('请输入以下信息，用空格分割')  # 输入提示
        input_str = input('文件大小（MB）  传输速度（Mbit/s）：')    # 输入内容赋值给变量input_str
        str_list = input_str.split(' ')    # 使用input.split 以空格分割输入的内容
        try:    # try 内的代码执行异常时，由except捕捉异常类型，并输出相应内容
            fs = float(str_list[0]) # 取第0位内容即文件大小，并将字符串类型转浮点类型
            ts = float(str_list[1]) # 取第1位内容即传输速度，并将字符串类型转浮点类型

            time = fs/(ts/8)

            print('传输时间为：{}秒（s）'.format(time)) # 使用{}占位，使用format方法格式化输出将()内的内容按顺序加到前面的{}中



        except ValueError:
            print('请检查文件大小，传输速度是否为数字')
        except:
            print('请输入正确的内容如：1 10')


        print() # 输出空行，以分割下一次用户执行
        yes_or_no = input('任意键继续，退出请输入no。')


if __name__ == "__main__":
    main()


