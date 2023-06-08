import os  # 导入os模块
import random
import sys

"""
完全随机模式
"""


def random_mode():
    # 清空控制台
    clear_console()

    # 生成一个整数列表list，它的值是随机的，应大于等于3不小于10
    floor = []

    # `_` 表示我们不打算在循环体内部使用循环变量的值
    for _ in range(random.randint(3, 10)):
        value = random.randint(3, 10)  # 生成数组元素的值，范围为3到10
        floor.append(value)


    # 画屋顶
    height = 5  # 屋顶的高度

    for i in range(1, height + 1):
        # 绘制屋顶的每一行
        spaces = "  " * (8 - (i + 2))  # 行前的空格
        stars = "*" * (6 * i - 1)  # 星号组成的行
        print(spaces + stars)

    # 画中间的楼层
    for index, x in enumerate(floor):
        print("*********************************")
        print("*\t\t%d楼\t\t*" % (index + 1))
        print("*\t\t%d 个\t\t*" % x)
        print("*\t\t\t\t*")
    print("*********************************")

    print()

    print("%d层的任意一层的钥匙都可以抽取，数量不超过3把，并且不小于1，胜利条件为："
          "最后一人如果抽到最后一个钥匙时，宣布成功" % len(floor))

    flag = True
    while flag:
        try:
            select_floor = input("请输入您要抽取的楼层, 输入n认输：")
            if select_floor == "n":
                print("你获胜了！")
                break
            if int(select_floor) < 1 or int(select_floor) > 10:
                print("数值非法，请重新输入")
                continue
        except ValueError:
            print("非法字符！请重新输入。")
            continue

        select_floor = int(select_floor)
        # 对应数组下标
        select_floor -= 1

        if floor[select_floor] > 0:
            # 清空控制台
            clear_console()

            # 画中间的楼层
            for index, x in enumerate(floor):
                print("*********************************")

                if select_floor == index:
                    print("*\t\t\t\t*         ****************")
                    print("*\t\t%d楼\t\t*\t*   已选中%d楼    *" % ((index + 1), (index + 1)))
                    print("*\t\t%d 个\t\t*         ****************" % x)
                else:
                    print("*\t\t\t\t*")
                    print("*\t\t%d楼\t\t*" % (index + 1))
                    print("*\t\t%d 个\t\t*" % x)
            print("*********************************")

            print("目前楼层为%d楼" % (select_floor + 1))
            select_key = int(input("请输入您要拿取的钥匙数量："))
            if select_key < 1 or select_key > 3 or floor[select_floor] - select_key < 0:
                print("钥匙数量非法，请重新输入")
                continue

            clear_console()

            # 减去对应楼层的钥匙数量
            floor[select_floor] -= select_key
            # 画目前的楼层
            for index, x in enumerate(floor):
                print("*********************************")

                if select_floor == index:
                    print("*\t\t\t\t*         *******************************")
                    print("*\t\t%d楼\t\t*\t*   已选中%d楼，拿取了%d把钥匙    *" % ((index + 1), (index + 1), select_key))
                    print("*\t\t%d 个\t\t*         *******************************" % x)
                else:
                    print("*\t\t\t\t*")
                    print("*\t\t%d楼\t\t*" % (index + 1))
                    print("*\t\t%d 个\t\t*" % x)
            print("*********************************")

            sumKey = sum(floor)
            if sumKey != 0:
                print("总共还剩%d把钥匙……" % sumKey)
            else:
                print("你获胜了！")


"""
默认选择模式
"""


def default_mode():
    # 清空控制台
    clear_console()

    # 对应楼层包含的钥匙数量
    # 不重复随机选择一个钥匙不为0的楼层
    # 经典模式，完全随机模式
    floor = [3, 3, 3]

    print("目前一楼的钥匙有%d把，二楼有%d把，三楼有%d把:" % (floor[0], floor[1], floor[2]))
    print("三层的任意一层的钥匙都可以抽取，数量不超过3把，并且不小于1."
          "胜利条件为：最后一人如果抽到最后一个钥匙时，宣布成功")

    flag = True

    while flag:
        try:
            select_floor = input("请输入您要抽取的楼层, 输入n认输：")
            if select_floor == "n":
                print("你获胜了！")
                break
            if int(select_floor) < 1 or int(select_floor) > 3:
                print("数值非法，请重新输入")
                continue
        except ValueError:
            print("非法字符！请重新输入。")
            continue

        select_floor = int(select_floor)
        # 对应数组下标
        select_floor -= 1

        print()
        print("目前楼层为%d楼" % (select_floor + 1))
        print()

        select_key = int(input("请输入您要拿取的钥匙数量："))
        if select_key < 1 or select_key > 3 or floor[select_floor] - select_key < 0:
            print("钥匙数量非法，请重新输入")
            continue

        clear_console()

        # 减去对应楼层的钥匙数量
        floor[select_floor] -= select_key

        print("目前一楼的钥匙有%d把，二楼有%d把，三楼有%d把。" % (floor[0], floor[1], floor[2]))
        sumKey = sum(floor)
        if sumKey != 0:
            print("总共还剩%d把钥匙……" % sumKey)
        else:
            print("你获胜了！")


def clear_console():
    if sys.platform.startswith('win'):  # Windows系统
        os.system('cls')
    else:  # 类Unix系统（如Linux、macOS）
        os.system('clear')


"""
3/n/3
平衡对决，后手反而成为先手
"""

if __name__ == '__main__':
    print("---------------摸钥匙--------------- \n"
          "1. 经典模式 \n"
          "2. 完全随机模式")
    flag = True
    while flag:
        try:
            print("请选择模式：")
            if int(input()) == 1:
                default_mode()
            else:
                random_mode()
            flag = False
        except ValueError:
            print("非法字符！请重新输入。")
