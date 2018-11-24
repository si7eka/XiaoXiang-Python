"""
    作者：李征
    功能：五角星绘图
    版本：1.0

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
"""

import turtle


def main():
    """
        主函数
    """

    count = 1   # 计数器

    while count <= 5:   # 当计数器小于等于5的时候执行下面循环

        # 第一条边，并转方向144度
        turtle.forward(100)
        turtle.right(144)
        count = count +1

    turtle.exitonclick()


if __name__ == "__main__":
    main()
