"""
============================================
题目：数据处理流水线
============================================
功能：读取CSV → 筛选 → 统计 → 生成报告
知识点：函数组合 / 流程控制 / 多步骤数据处理
"""

import os


def read_csv(filepath):
    """
    读取CSV文件，返回表头和数据列表
    
    参数：
        filepath: 文件路径
    
    返回：
        header: 表头列表，如 ["姓名", "班级", "分数"]
        data: 数据列表，每条数据是一个字典
              如 [{"姓名": "张三", "班级": "一班", "分数": 85}, ...]
    
    文件不存在时返回：None, None
    """
    # 检查文件是否存在
    if not os.path.exists(filepath):
        print(f"文件:{filepath}不存在")
        return None, None
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        # 第一行是表头
        header = lines[0].strip().split(",")
        data = []
        
        # 从第2行开始是数据
        for line in lines[1:]:
            line = line.strip()
            if line == "":      # 跳过空行
                continue
            
            parts = line.split(",")
            row = {}
            for i in range(len(header)):
                if header[i] == "分数":
                    row[header[i]] = int(parts[i])   # 分数转整数
                else:
                    row[header[i]] = parts[i]
            data.append(row)
    
    return header, data


def calc_stats(data):
    """
    计算统计信息
    
    参数：
        data: 数据列表
    
    返回：
        dict: {"总人数": x, "平均分": x, "最高分": x, "最低分": x}
    """
    scores = []
    for row in data:
        scores.append(row["分数"])
    
    count = len(scores)
    total = sum(scores)
    avg = total / count
    maxscore = max(scores)
    minscore = min(scores)
    
    return {
        "总人数": count,
        "平均分": avg,
        "最高分": maxscore,
        "最低分": minscore
    }


def filter_by_score(data, min_score=80):
    """
    筛选分数高于指定值的学生
    
    参数：
        data: 数据列表
        min_score: 最低分数线，默认80
    
    返回：
        list: 筛选后的数据列表
    """
    filtered = [x for x in data if x["分数"] >= min_score]
    return filtered


def generate_report(data, stats, output_file):
    """
    生成文本报告
    
    参数：
        data: 数据列表
        stats: 统计信息字典
        output_file: 输出文件路径
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("成绩报告\n")
        f.write(f"总人数：{stats['总人数']}\n")
        f.write(f"平均分：{stats['平均分']}\n")
        f.write(f"最高分：{stats['最高分']}\n")
        f.write(f"最低分：{stats['最低分']}\n")
        f.write("\n学生名单:\n")
        for row in data:
            f.write(f"{row['姓名']} {row['班级']} {row['分数']}\n")


def process_pipeline(input_file, output_folder="output", min_score=80):
    """
    主函数：一键完成所有步骤
    
    参数：
        input_file: 输入CSV文件路径
        output_folder: 输出文件夹，默认"output"
        min_score: 筛选分数线，默认80分
    
    返回：
        dict: 统计信息
    """
    # 1. 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 2. 读取数据
    header, data = read_csv(input_file)
    if data is None:
        return None
    
    # 3. 统计分析
    stats = calc_stats(data)
    
    # 4. 筛选高分学生
    filtered = filter_by_score(data, min_score)
    
    # 5. 保存筛选结果
    filterfile = os.path.join(output_folder, "filtered.csv")
    with open(filterfile, "w", encoding="utf-8") as f:
        f.write("姓名,班级,分数\n")
        for row in filtered:
            f.write(f"{row['姓名']},{row['班级']},{row['分数']}\n")
    
    # 6. 生成报告
    report_file = os.path.join(output_folder, "report.txt")
    generate_report(filtered, stats, report_file)
    
    return stats
