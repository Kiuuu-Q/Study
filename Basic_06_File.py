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




练习
"""
============================================
题目：文件备份工具
============================================
功能：自动备份文件到指定文件夹，文件名加日期时间戳
知识点：os.path / datetime / 文件读写
"""

import os
from datetime import datetime

def backup_file(filepath, backup_folder="backup"):
    """
    备份文件到指定文件夹，文件名加日期时间戳
    参数：filepath-文件路径, backup_folder-备份文件夹名
    返回：成功True，失败False
    """
    # 1. 检查源文件是否存在
    if not os.path.exists(filepath):
        print(f"错误：文件 {filepath} 不存在")
        return False
    
    # 2. 生成带时间戳的新文件名
    now = datetime.now()
    date_str = now.strftime("%Y%m%d")  # "20260828"
    
    filename = os.path.basename(filepath)  # "scores.txt"
    parts = filename.split(".")            # ["scores", "txt"]
    name = parts[0]                        # "scores"
    ext = parts[1]                         # "txt"
    
    newname = f"{name}-{date_str}-{ext}"   # "scores-20260828-txt"
    
    # 3. 创建备份文件夹（exist_ok=True 防止已存在时报错）
    os.makedirs(backup_folder, exist_ok=True)
    
    # ⚠️ 易错点：os.path.join(文件夹, 文件名)，不是 join(文件路径, 文件名)
    newfile = os.path.join(backup_folder, newname)
    
    # 4. 复制文件
    try:
        with open(filepath, "r", encoding="utf-8") as fin:
            content = fin.read()
        
        with open(newfile, "w", encoding="utf-8") as fout:
            fout.write(content)
        
        print(f"备份成功：{newfile}")
        return True
    except Exception as e:
        print(f"备份失败：{e}")
        return False


# ========== 测试 ==========
if __name__ == "__main__":
    backup_file("scores.txt")
    backup_file("notexist.txt")
    backup_file("scores.txt", "my_backup")






"""
============================================
题目：批量备份工具
============================================
功能：备份文件夹内所有 .txt 文件
知识点：os.listdir() / os.path.isfile() / .endswith()
"""

import os
from datetime import datetime


# ========== 函数1：备份单个文件（昨天写的）==========
def backup_file(filepath, backup_folder="backup"):
    """备份单个文件，文件名加时间戳"""
    if not os.path.exists(filepath):
        print(f"错误：文件 {filepath} 不存在")
        return False

    # 生成带时间戳的新文件名
    now = datetime.now()
    date_str = now.strftime("%Y%m%d")

    filename = os.path.basename(filepath)
    parts = filename.split(".")
    name = parts[0]
    ext = parts[1]
    newname = f"{name}-{date_str}-{ext}"

    # 创建备份文件夹
    os.makedirs(backup_folder, exist_ok=True)

    # ⚠️ 易错点：os.path.join(文件夹, 文件名)，不是 join(文件路径, 文件名)
    newfile = os.path.join(backup_folder, newname)

    # 复制文件
    try:
        with open(filepath, "r", encoding="utf-8") as fin:
            content = fin.read()

        with open(newfile, "w", encoding="utf-8") as fout:
            fout.write(content)

        print(f"备份成功：{newfile}")
        return True
    except Exception as e:
        print(f"备份失败：{e}")
        return False


# ========== 函数2：批量备份（今天写的）==========
def batch_backup(folder_path, backup_folder="backup"):
    """
    批量备份文件夹内所有 .txt 文件

    参数：
        folder_path: 要备份的文件夹路径
        backup_folder: 备份目标文件夹

    返回：
        {"成功": 数量, "失败": 数量, "文件列表": [...]}
    """
    # 1. 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 {folder_path} 不存在")
        return {"成功": 0, "失败": 0, "文件列表": []}

    # 2. 列出文件夹所有内容
    items = os.listdir(folder_path)

    # 3. 筛选出所有 .txt 文件
    txt_files = []
    for item in items:
        full_path = os.path.join(folder_path, item)
        # ⚠️ 必须用完整路径判断！os.path.isfile() 需要完整路径
        if os.path.isfile(full_path) and item.endswith(".txt"):
            txt_files.append(full_path)  # 存完整路径，方便后面直接操作

    # 4. 如果没有 txt 文件
    if not txt_files:
        print("未找到任何 .txt 文件")
        return {"成功": 0, "失败": 0, "文件列表": []}

    # 5. 逐个备份
    succeed = 0
    unsuc = 0
    file_list = []

    for filepath in txt_files:
        # ⚠️ 必须传完整路径！
        result = backup_file(filepath, backup_folder)
        filename = os.path.basename(filepath)
        file_list.append(filename)

        if result:
            succeed += 1
        else:
            unsuc += 1

    # 6. 返回汇总结果
    return {"成功": succeed, "失败": unsuc, "文件列表": file_list}


# ========== 测试 ==========
if __name__ == "__main__":
    # 批量备份
    result = batch_backup("data", "backup")
    print(result)
