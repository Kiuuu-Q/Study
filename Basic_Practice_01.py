张三,一班,85
李四,二班,92
王五,一班,78
赵六,三班,65
孙七,二班,88
周八,一班,59

函数1：read_scores(filepath)
读取文件，返回字典 {姓名: {"班级": 班级, "分数": 分数}}
如果文件不存在，返回 None
空行跳过

def read_scores(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            result = {}

            for line in lines:
                line = line.strip()  # ✅ 加括号
                if line == "":
                    continue

                try:
                    parts = line.split(",")
                    name = parts[0]
                    classname = parts[1]
                    score = int(parts[2])  # 变量名统一
                    result[name] = {"班级": classname, "分数": score}  # ✅ 用冒号
                except (ValueError, IndexError):  # ✅ 正确格式
                    continue

            return result

    except FileNotFoundError:
        return None


函数2：get_class_avg(scores_dict, class_name)
需求
传入函数1返回的字典，计算指定班级的平均分。如果班级不存在，返回 0。


def get_class_avg(scores_dict, class_name):
    total = 0
    count = 0

    for name, info in scores_dict.items():
        if info["班级"] == class_name:
            total = total + info["分数"]
            count = count + 1

    if count == 0:
        return 0
    else:
        return total / count


函数3：
def save_summary(scores_dict, output_file):
    try:
        # 1. 找出所有班级（去重）
        classes = []
        for name, info in scores_dict.items():
            if info["班级"] not in classes:
                classes.append(info["班级"])
        
        # 2. 打开文件准备写入
        with open(output_file, "w", encoding="utf-8") as f:
            # 3. 遍历每个班级
            for cls in classes:
                # 4. 调用函数2计算平均分
                avg = get_class_avg(scores_dict, cls)
                # 5. 写入文件
                f.write(f"{cls}: {avg}\n")
        
        return True
    except:
        return False
