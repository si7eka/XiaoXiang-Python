"""
    作者：Si7eka
    功能：计算用户BMR
    版本：4.0


"""
def main():
    """
    主函数
    """
    yes_or_no = input('输入任意键继续，退出请输入no。')

    while yes_or_no != "no":
        print('请输入以下信息，用空格分割')  # 输入提示
        input_str = input('性别 体重（KG） 身高（cm） 年龄：')    # 输入内容赋值给变量input_str
        str_list = input_str.split(' ')    # 使用input.split 以空格分割输入的内容
        try:    # try 内的代码执行异常时，由except捕捉异常类型，并输出相应内容
            gender = str_list[0]    # 取前面的分割第0位内容即性别
            weight = float(str_list[1]) # 取第1位内容即体重，并将字符串类型转浮点类型
            height = float(str_list[2]) # 取第2位内容即身高，并将字符串类型转浮点类型
            age = int(str_list[3])  # 取第3位内容即年龄，并将字符串类型转整数型

            if gender == "男": # 如果性别等于 男 则按下面公式计算bmr
                # 男性
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            elif gender == "女": #  再或者性别等于 女 则按下面公式计算bmr
                # 女性
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
            else:   # 否则bmr赋值-1
                bmr = -1


            if bmr != -1: # 如果bmr不等于 -1 则输出下面的内容
                print('您的性别：{}，体重：{}KG，身高：{}cm，年龄：{}岁'.format(gender,weight,height,age)) # 使用{}占位，使用format方法格式化输出将()内的内容按顺序加到前面的{}中
                print('您的基础代谢率：{}大卡 '.format(bmr))
            else:    # 否则输出下面内容
                print('暂不支持这个类型')

        except ValueError:
            print('请检查体重，身高，年龄等是否为数字')
        except:
            print('请输入正确的内容如：男 60 175 23')


        print() # 输出空行，以分割下一次用户执行
        yes_or_no = input('任意键继续，退出请输入no。')


if __name__ == "__main__":
    main()
