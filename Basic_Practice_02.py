"""
============================================
数据分析工具集
功能：读取成绩文件 + 统计分析
日期：2026-08-26
============================================
"""

# ==========================================
# 函数1：read_scores(filepath)
# 作用：读取成绩文件，返回字典
# ==========================================

def read_scores(filepath):
    """
    读取成绩文件，返回字典格式的数据
    
    参数：
        filepath (str): 文件路径，如 "scores.txt"
    
    返回：
        dict: {姓名: {"班级": 班级, "分数": 分数}}
        如果文件不存在，返回 None
    
    文件格式要求：
        每行格式：姓名,班级,分数
        例如：张三,一班,85
    
    异常处理：
        - 文件不存在 → 返回 None
        - 空行 → 跳过
        - 格式错误（如缺少逗号）→ 跳过该行
    """
    try:
        # 打开文件，使用 utf-8 编码防止中文乱码
        with open(filepath, "r", encoding="utf-8") as f:
            # readlines() 读取所有行，每行作为一个字符串，包含末尾的 \n
            lines = f.readlines()
            
            # 初始化空字典，用于存放结果
            result = {}
            
            # 逐行处理
            for line in lines:
                # strip() 去掉字符串首尾的空白字符（包括 \n 和空格）
                line = line.strip()
                
                # 如果是空行（如文件末尾的换行），跳过
                if line == "":
                    continue
                
                # 内层 try：处理单行数据格式错误
                try:
                    # split(",") 按逗号分割，返回列表
                    # 例如 "张三,一班,85" → ["张三", "一班", "85"]
                    parts = line.split(",")
                    
                    # 解包赋值，依次取出姓名、班级、分数
                    name = parts[0]
                    class_name = parts[1]
                    # 注意：分数要转成整数 int()，否则是字符串
                    score = int(parts[2])
                    
                    # 存入字典
                    # 格式：{"姓名": {"班级": 班级, "分数": 分数}}
                    result[name] = {"班级": class_name, "分数": score}
                    
                except (ValueError, IndexError):
                    # ValueError: 分数无法转成 int（如 "abc"）
                    # IndexError: split 后元素不够（如缺少逗号）
                    # 遇到坏数据直接跳过，不影响其他行
                    continue
            
            # 循环结束，返回字典
            return result
    
    except FileNotFoundError:
        # 文件不存在时返回 None，调用方需要检查
        return None


# ==========================================
# 函数2：calc_stat(numlist, even=False, need_std=False)
# 作用：统计数字列表的指标
# ==========================================

import math  # 导入 math 库用于开平方

def calc_stat(numlist, even=False, need_std=False):
    """
    对数字列表进行统计分析
    
    参数：
        numlist (list): 数字列表，如 [85, 92, 78]
        even (bool): 统计类型
            - False（默认）：统计小于平均值的奇数个数
            - True：统计小于平均值的偶数个数
        need_std (bool): 是否返回标准差
            - False（默认）：不返回标准差
            - True：额外返回标准差
    
    返回：
        如果 need_std=False: (奇数/偶数个数, 总和, 总个数, 平均值)
        如果 need_std=True:  (奇数/偶数个数, 总和, 总个数, 平均值, 标准差)
    
    核心逻辑：
        1. 计算所有数字的总和、个数、平均值
        2. 找出所有小于平均值的数字
        3. 从这些数字中筛选奇数或偶数
        4. 统计个数并返回
        5. 如果 need_std=True，额外计算标准差
    """
    # --- 第一步：基本统计量 ---
    total = sum(numlist)      # 总和
    count = len(numlist)      # 个数
    avg = total / count       # 平均值
    
    # --- 第二步：筛选小于平均值的数 ---
    # 列表推导式：遍历 numlist，只保留 x < avg 的元素
    filtered = [x for x in numlist if x < avg]
    
    # --- 第三步：分成奇数和偶数 ---
    # 判断奇数：x % 2 != 0（除以2余数不为0）
    odds = [x for x in filtered if x % 2 != 0]
    # 判断偶数：x % 2 == 0（除以2余数为0）
    evens = [x for x in filtered if x % 2 == 0]
    
    # --- 第四步：根据 even 参数选择统计哪个 ---
    if even:
        # even=True → 统计偶数个数
        c = len(evens)
    else:
        # even=False → 统计奇数个数（默认）
        c = len(odds)
    
    # --- 第五步：如果需要，计算标准差 ---
    if need_std:
        # 标准差公式：sqrt( 每个数与平均值的差的平方之和 / 个数 )
        # 步骤：
        #   1. (x - avg) ** 2      每个数与平均值的差的平方
        #   2. sum(...)            求和
        #   3. / count             除以个数
        #   4. math.sqrt(...)      开平方
        std = math.sqrt(sum((x - avg) ** 2 for x in numlist) / count)
        # 返回 5 个值
        return c, total, count, avg, std
    else:
        # 返回 4 个值
        return c, total, count, avg


# ==========================================
# 函数3：analyze_from_file(filepath, even=False, need_std=False)
# 作用：读取文件 + 数据分析 的组合函数
# ==========================================

def analyze_from_file(filepath, even=False, need_std=False):
    """
    从文件读取数据并进行分析（函数1 + 函数2 的组合）
    
    参数：
        filepath (str): 文件路径
        even (bool): 是否统计偶数（默认 False，统计奇数）
        need_std (bool): 是否返回标准差（默认 False）
    
    返回：
        如果文件不存在：返回 None
        否则：返回 calc_stat 的结果
            - need_std=False: (个数, 总和, 总个数, 平均值)
            - need_std=True:  (个数, 总和, 总个数, 平均值, 标准差)
    
    执行流程：
        read_scores() → 得到字典 → 提取所有分数 → calc_stat() → 返回结果
    """
    # 步骤1：调用 read_scores 读取文件
    data = read_scores(filepath)
    
    # 步骤2：如果文件不存在，read_scores 返回 None
    if data is None:
        return None
    
    # 步骤3：从字典中提取所有分数，组成列表
    scores = []
    # data.items() 遍历每个键值对
    # name: "张三", info: {"班级": "一班", "分数": 85}
    for name, info in data.items():
        # 注意：info 是字典，用 ["分数"] 取值
        scores.append(info["分数"])
    # 此时 scores = [85, 92, 78, 65, 88, 59]
    
    # 步骤4：调用 calc_stat 进行统计分析
    # 把 even 和 need_std 原样传递
    result = calc_stat(scores, even, need_std)
    
    # 步骤5：返回结果
    return result


# ==========================================
# 测试代码（可选）
# ==========================================

if __name__ == "__main__":
    # 测试函数1
    print("=== 测试 read_scores ===")
    data = read_scores("scores.txt")
    print(data)
    
    # 测试函数2
    print("\n=== 测试 calc_stat ===")
    test_data = [1, 3, 2, 6, 65, 34]
    c, total, count, avg = calc_stat(test_data)
    print(f"奇数个数:{c}, 总和:{total}, 总数:{count}, 平均:{avg}")
    
    # 测试函数3
    print("\n=== 测试 analyze_from_file ===")
    c, total, count, avg = analyze_from_file("scores.txt")
    print(f"奇数个数:{c}, 总和:{total}, 总数:{count}, 平均:{avg}")
