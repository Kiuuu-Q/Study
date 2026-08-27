

# 读取
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 全部内容（字符串）
    lines = f.readlines()     # 按行读取（列表）
# 写入
#1
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")       # 手动加换行
    f.write("第二行\n")
#2
data = ["苹果", "香蕉", "橙子"]
with open("out.txt", "w", encoding="utf-8") as f:
    for item in data:
        f.write(item + "\n")


# 追加
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("新增一行\n")

