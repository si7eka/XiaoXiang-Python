"""
    作者：李征
    功能：五角星绘图
    版本：3.0
    新增：循环操作
    新增：迭代函数（递归函数）

    turtle库说明：
    形状绘制函数
        turtle.forward(distance)
        画笔向前移动distance距离
        turtle.backward(distance)
        笔画向后移动distance距离
        turtle.right(degree)
        绘制方向向右旋转degree度
        turtle.exitonclick()
        点击关闭图形窗口

                     （左）
                       |
              （后）--中心点--（前）
                       |
                     （右）
        更多查询 https://docs.python.org/3/library/turtle.html#module-turtle
"""

import turtle


def huizhi_wujiaoxing_diguihanshu(size):
    # 绘制五角星
    count = 1  # 计数器
    while count <= 5:     # 计数器小于等于5的时候执行循环
        turtle.forward(size)    # 绘图向前size的长度
        turtle.right(144)   # 右转144度
        count += 1   # 计数器+1 相当于 count = count + 1

    # 五角星绘制完成，并传新的size参数进函数
    size += 30  # 参数+30 后在赋值给自己
    if size <= 170:  #如果size 小于等于170，执行函数自己
        huizhi_wujiaoxing_diguihanshu(size)



def main():
    """
        主函数
    """


    size = 50   # 星星边长初始尺寸
    huizhi_wujiaoxing_diguihanshu(size)
    turtle.exitonclick()    # 点击关闭图形


if __name__ == "__main__":
    main()
