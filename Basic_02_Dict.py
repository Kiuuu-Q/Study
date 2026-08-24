1.创建字典

#方法1：直接写
d = {"name": "小明", "age": 18}
# 方法2：空字典，慢慢添加
d = {}
d["name"] = "小明"
d["age"] = 18
# 方法3：用 dict() 函数
d = dict(name="小明", age=18)  # 注意：这里键不用加引号

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


