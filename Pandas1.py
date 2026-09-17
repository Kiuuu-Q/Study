day1
1.读取csv
import pandas as pd
df = pd.read_csv("students.csv", encoding="utf-8")

2.查看数据
df.head()        # 前5行
df.tail()        # 后5行
df.shape         # (行数, 列数)
df.columns       # 列名
df.info()        # 数据类型
df.describe()    # 统计描述

3.筛选数据
df[df["分数"] >= 80]                     # 分数>=80
df[df["班级"] == "一班"]                  # 班级是一班
df[(df["分数"] >= 80) & (df["班级"] == "一班")]  # 多条件

4.统计
df["分数"].mean()    # 平均分
df["分数"].max()     # 最高分
df["分数"].min()     # 最低分
df["分数"].sum()     # 总分
df["分数"].count()   # 人数

5.分组统计
df.groupby("班级")["分数"].mean()    # 每班平均分
df.groupby("班级")["分数"].max()     # 每班最高分
df.groupby("班级")["分数"].count()   # 每班人数
df.groupby("班级")["分数"].agg(["mean", "max", "count"])  # 多个统计

6.排序
df.sort_values("分数")                    # 升序
df.sort_values("分数", ascending=False)   # 降序

7.新增列
def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

df["等级"] = df["分数"].apply(get_grade)

8.保存csv
df.to_csv("output.csv", index=False, encoding="utf-8-sig")
# index=False：不保存行号
# encoding="utf-8-sig"：防止Excel打开乱码

"""
============================================
题目：按班级分组分析成绩
============================================
功能：读取CSV → 按班级分组 → 排序 → 新增等级 → 保存
知识点：pandas groupby / sort_values / apply / to_csv
"""

import os
import pandas as pd


def analyze_by_class(filepath, output_folder="output"):
    """
    按班级分组分析成绩
    
    参数：
        filepath: CSV文件路径
        output_folder: 输出文件夹
    
    返回：
        dict: 每个班级的统计信息
    """
    # 1. 检查文件是否存在
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"文件 {filepath} 不存在")
    
    # 2. 读取CSV
    df = pd.read_csv(filepath, encoding="utf-8")
    
    # 3. 按班级分组统计
    result = df.groupby("班级")["分数"].agg(["mean", "max", "count"])
    result = result.sort_values("mean", ascending=False)
    print(result)
    
    # 4. 新增"等级"列
    def get_grade(score):
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"
    
    df["等级"] = df["分数"].apply(get_grade)
    
    # 5. 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 6. 保存两个文件
    class_file = os.path.join(output_folder, "class_report.csv")
    result.to_csv(class_file, encoding="utf-8-sig")
    
    student_file = os.path.join(output_folder, "students_with_grade.csv")
    df.to_csv(student_file, index=False, encoding="utf-8-sig")
    
    # 7. 返回统计结果
    return result.to_dict()


# 测试
if __name__ == "__main__":
    result = analyze_by_class("students.csv")
    print(result)



day2
1.查看缺失
df.isnull()              # 每个位置是否为空
df.isnull().sum()        # 每列空值数
df.isnull().sum().sum()  # 总共多少空值

2.处理缺失
df.dropna()                          # 删除任何含空值的行
df.dropna(subset=["分数"])           # 只删分数为空的行
df.fillna(0)                         # 空值填0
df["分数"].fillna(df["分数"].mean())  # 用平均分填

3.处理重复
df.duplicated()              # 每行是否重复
df.duplicated().sum()        # 重复行数
df.drop_duplicates()         # 删除重复行
df.drop_duplicates(subset=["姓名"])  # 按姓名去重

4.类型转换
df["分数"].astype(int)                    # 转整数
pd.to_numeric(df["分数"], errors="coerce")  # 无法转的变NaN

5.字符串处理
df["姓名"].str.strip()              # 去首尾空格
df["班级"].str.replace("班", "")    # 替换字符
df["姓名"].str.contains("张")       # 是否包含"张"

"""
============================================
题目：数据清洗工具
============================================
功能：清洗脏数据（空值、重复、格式错误）
知识点：pandas to_numeric / dropna / drop_duplicates / str.strip
"""

import os
import pandas as pd


def clean_data(filepath, output_file):
    """
    清洗脏数据
    
    参数：
        filepath: 输入CSV文件路径
        output_file: 输出文件路径
    
    返回：
        dict: 清洗报告
    """
    # 1. 检查文件是否存在
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"文件 {filepath} 不存在")
    
    # 2. 读取数据
    df = pd.read_csv(filepath, encoding="utf-8")
    original = len(df)
    
    # 3. 统计空值和重复数（清洗前）
    null_count = df.isnull().sum().sum()
    dup_count = df.duplicated().sum()
    
    # 4. 分数转数字（abc → NaN）
    df["分数"] = pd.to_numeric(df["分数"], errors="coerce")
    
    # 5. 删除分数为空的行
    df = df.dropna(subset=["分数"])
    
    # 6. 删除重复行
    df = df.drop_duplicates()
    
    # 7. 去掉姓名首尾空格
    df["姓名"] = df["姓名"].str.strip()
    
    # 8. 保存
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    
    # 9. 返回清洗报告
    return {
        "原始行数": original,
        "空值数": null_count,
        "重复数": dup_count,
        "最终行数": len(df)
    }


# 测试
if __name__ == "__main__":
    result = clean_data("dirty.csv", "clean.csv")
    print(result)





day3(多表操作）
1.手动读取
import pandas as pd

df1 = pd.read_csv("data/class1.csv")
df2 = pd.read_csv("data/class2.csv")
df3 = pd.read_csv("data/class3.csv")

df_all = pd.concat([df1, df2, df3], ignore_index=True)


2.自动读取
import os
import pandas as pd

folder = "data"
all_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

dfs = []
for file in all_files:
    path = os.path.join(folder, file)
    df = pd.read_csv(path)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)


3.拼接
上下：
result = pd.concat([df1, df2])                     # 索引重复
result = pd.concat([df1, df2], ignore_index=True)  # 重新编号

左右
result = pd.concat([df1, df2], axis=1)

merge关联
result = pd.merge(df1, df2, on="姓名", how="inner")

4.查看合并结果
df_all.shape                # (行数, 列数)
df_all.head()               # 看前5行
df_all.tail()               # 看后5行
df_all.duplicated().sum()   # 重复行数
df_all.drop_duplicates()    # 删除重复
df_all.info()               # 数据类型
df_all.describe()           # 统计信息


5.分组后导出多个文件
os.makedirs("output", exist_ok=True)

for cls, group in df.groupby("班级"):
    filename = os.path.join("output", f"{cls}.csv")
    group.to_csv(filename, index=False, encoding="utf-8-sig")

"""
============================================
题目：多班级成绩汇总分析
============================================
功能：合并文件夹内所有CSV，按班级分组导出并汇总
知识点：pd.concat / drop_duplicates / groupby / to_csv
"""

import os
import pandas as pd


def merge_and_analyze(folder_path, output_folder="output"):
    """
    合并文件夹内所有CSV成绩文件，并分析
    
    参数：
        folder_path: 包含多个CSV的文件夹
        output_folder: 输出文件夹
    
    返回：
        dict: 汇总信息
    """
    # 1. 检查文件夹是否存在
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"文件夹 {folder_path} 不存在")
    
    # 2. 列出所有CSV文件
    all_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    
    if not all_files:
        print("未找到任何 CSV 文件")
        return None
    
    # 3. 逐个读取并合并
    dfs = []
    for file in all_files:
        path = os.path.join(folder_path, file)
        df = pd.read_csv(path)
        dfs.append(df)
    
    df_all = pd.concat(dfs, ignore_index=True)
    
    # 4. 去重
    df_all = df_all.drop_duplicates()
    
    # 5. 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 6. 按班级分组导出
    for cls, group in df_all.groupby("班级"):
        filename = os.path.join(output_folder, f"{cls}.csv")
        group.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"已导出：{filename}")
    
    # 7. 生成汇总表
    summary = df_all.groupby("班级")["分数"].agg(["mean", "max", "count"])
    summary_file = os.path.join(output_folder, "summary.csv")
    summary.to_csv(summary_file, encoding="utf-8-sig")
    
    # 8. 返回汇总信息
    return {
        "总人数": len(df_all),
        "班级数": len(summary),
        "最高分": df_all["分数"].max()
    }


# 测试
if __name__ == "__main__":
    result = merge_and_analyze("data")
    print(result)


















