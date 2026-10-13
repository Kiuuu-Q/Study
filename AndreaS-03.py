Chap03

金字塔：
def triangle(x, y):
    for i in range(1, y + 1):
        print(x * i)

triangle("M", 5)
输出
M
MM
MMM
MMMM
MMMMM


矩形：
def rectangle(x, y, z):
    # 第一行：字符重复 y 次
    print(x * y)
    # 中间 z-2 行：字符 + (y-2)个空格 + 字符
    for i in range(z - 2):
        print(x + " " * (y - 2) + x)
    # 最后一行
    print(x * y)

rectangle("h", 5, 4)
输出
hhhhh
h   h
h   h
hhhhh
