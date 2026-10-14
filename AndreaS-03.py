Chap03


编写函数print_right，接受字符串形参text，打印该字符串，用空格填充左边，从而让text中的最后一个字母出现在一行的第40列。
def print_right(text):
    print(" " * (40 - len(text)) + text)

print_right("nana")

                          nana



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

如果要反过来：
list(range(5,0,-1)) #[5,4,3,2,1]
so:
for i in range(y,0,-1):
    prnit(x*i)


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
