"""
    作者：李征
    功能：五角星绘图
    版本：2.0
    新增：循环操作

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


def huizhi_wujiaoxing(size):
    # 绘制五角星
    count = 1  # 计数器
    while count <= 5:     # 计数器小于等于5的时候执行循环
        turtle.forward(size)    # 绘图向前size的长度
        turtle.right(144)   # 右转144度
        count += 1   # 计数器+1 相当于 count = count + 1



def main():
    """
        主函数
    """



    size = 50   # 星星边长初始尺寸

    while size <= 170:    # 边长小于等于200的执行循环
        # 调用函数
        huizhi_wujiaoxing(size)
        size += 30    # 执行完绘制五星之后边长+30

    turtle.exitonclick()    # 点击关闭图形


if __name__ == "__main__":
    main()
