"""
    作者：李征
    功能：利用递归绘制分形树
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
        更多查询 https://docs.python.org/3/library/turtle.html#module-turtle
"""

import turtle


def huizhi_fenxingshu_shuzhi(shuzhichangdu, shuzhisize):
    """
    绘制分形树
    """

    if shuzhichangdu > 5:


        # 绘制右侧树枝
        turtle.pensize(shuzhisize)
        turtle.forward(shuzhichangdu)
        turtle.right(20)
        huizhi_fenxingshu_shuzhi(shuzhichangdu - 15, shuzhisize - 1)
        if shuzhisize < 3:
            turtle.color("green")
        # 绘制左侧树枝
        turtle.left(40)
        huizhi_fenxingshu_shuzhi(shuzhichangdu - 15, shuzhisize - 1)

        # 返回树杈节点
        if shuzhisize > 3:
            turtle.color("brown")
        turtle.right(20)
        turtle.backward(shuzhichangdu)

def main():
    """
        主函数
    """
    turtle.color("brown")

    turtle.left(90)
    huizhi_fenxingshu_shuzhi(shuzhichangdu=90, shuzhisize=7)
    turtle.exitonclick()    # 点击关闭图形


if __name__ == "__main__":
    main()
