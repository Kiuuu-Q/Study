1.创建字典

#方法1：直接写
d = {"name": "小明", "age": 18}

# 方法2：空字典，慢慢添加
d = {}
d["name"] = "小明"
d["age"] = 18

# 方法3：用 dict() 函数
d = dict(name="小明", age=18)  # 注意：这里键不用加引号

#方法4
fromkeys
作用：用一堆键，快速生成一个字典，值全部一样。
用法：dict.fromkeys(['a', 'b'], 0) 会生成 {'a': 0, 'b': 0}。注意这个是类方法，用 dict 调。
fromkeys（keys）——> {k1:None,k2:None,k3:None}


2.取值

d = {"name": "小明", "age": 18, "city": "北京"}
# 方式1：用 [键] （键必须存在，否则报错）
d["name"]   # "小明"
d["gender"] # ❌ KeyError! 程序崩溃
# 方式2：用 .get(键, 默认值) （键不存在返回默认值，不报错）✅ 推荐
d.get("name")          # "小明"
d.get("gender")        # None（不报错）
d.get("gender", "未知") # "未知"（返回自定义默认值）

3.修改

d = {"name": "小明", "age": 18}

# 修改已存在的键
d["age"] = 19    # {"name": "小明", "age": 19}
# 新增不存在的键（直接用赋值）
d["city"] = "北京"  # {"name": "小明", "age": 19, "city": "北京"}

#删除
del d["age"]
student.pop("gender", None) # 安全删除，找不到也不会报错
作用：弹出并删除指定的键，返回对应的值。
popitem：

#update
d.update({'c': 3, 'a': 99})。如果 'c' 不存在就加进去，如果 'a' 存在就把原来的 1 覆盖成 99。

4.遍历

d = {"name": "小明", "age": 18, "city": "北京"}
# 遍历所有键（最常用）
for key in d:
    print(key, d[key])  # name 小明 / age 18 / city 北京
# 遍历所有值
for value in d.values():
    print(value)  # 小明 / 18 / 北京
# 遍历键值对（最推荐）
for key, value in d.items():
    print(f"{key}: {value}")  # name: 小明 / age: 18 / city: 北京

5.嵌套字典取值

users = {
    "小明": {"age": 18, "city": "北京"},
    "小红": {"age": 20, "city": "上海"}
}
# 取小明的年龄
users["小明"]["age"]    # 18
# 取小红的城市
users["小红"]["city"]   # "上海"
# 安全的写法（防止键不存在）
users.get("小明", {}).get("age", 0)  # 18
users.get("王五", {}).get("age", 0)  # 0（不报错）


6.进阶用法

# 把列表变成字典：键是单词，值是单词长度
words = ["apple", "banana"]
word_len = {w: len(w) for w in words}
# 结果: {'apple': 5, 'banana': 6}



# 经典应用：把一堆单词按首字母分组
words = ["ant", "apple", "bat"]
groups = {}
for w in words:
    first_letter = w[0]
    # 如果 first_letter 不在字典里，先建一个空列表 []，然后把 w 加进去
    groups.setdefault(first_letter, []).append(w)
    结果: {'a': ['ant', 'apple'], 'b': ['bat']}


！！！！！！！！！！
如果是一对一（比如：学号 -> 成绩），用字典推导式。
如果是一对多（比如：班级 -> 该班所有学生名单），用 setdefault（或者 if not in 判断）。


#判断是否存在
if "name" in student:
    print("找到了！")



#完整题目
def analyze_logs(logs):
    d = {}
    for log in logs:
        # 1. 切分用户名和动作，并清理空格和大小写
        parts = log.split(":")
        user = parts[0].strip().lower()
        action = parts[1].strip().lower()
        
        # 2. 用 setdefault 分组（初始化空列表）
        d.setdefault(user, [])
        
        # 3. 去重：如果动作不在列表里，才加进去
        if action not in d[user]:
            d[user].append(action)
            
    # 4. 遍历字典，对每个动作列表排序
    for actions in d.values():
        actions.sort()
        
    return d














