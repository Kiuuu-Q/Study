1

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

2.Ospath

import os
# 1. 检查文件/文件夹是否存在
os.path.exists("scores.txt")        # True/False
# 2. 获取文件名（去掉路径）
os.path.basename("data/scores.txt") # "scores.txt"
# 3. 获取文件所在目录
os.path.dirname("data/scores.txt")  # "data"
# 4. 拼接路径（跨平台）
os.path.join("backup", "scores.txt")  # "backup/scores.txt"
# 5. 创建文件夹（自动创建不存在的父目录）
os.makedirs("backup/2026", exist_ok=True)


3.datetime

from datetime import datetime
# 获取当前日期
now = datetime.now()
print(now)  # 2026-08-28 14:30:25.123456
# 格式化日期（只取年月日）
date_str = now.strftime("%Y%m%d")
print(date_str)  # "20260828"
# 更多格式：
# %Y = 年（4位）, %m = 月, %d = 日
# %H = 时, %M = 分, %S = 秒
