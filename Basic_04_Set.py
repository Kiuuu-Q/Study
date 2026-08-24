1.自动去重
2.无序
3.元素必须不可变
# 可以放数字、字符串、元组
s = {1, "hello", (1, 2)}  # OK
# 不能放列表、字典（可变类型）
s = {1, [1, 2]}   # TypeError: unhashable type: 'list'
s = {1, {"a": 1}} # TypeError: unhashable type: 'dict'

4.
#增加
s={1，2，3}
s.add（4）
#删除
s.remove（10）#会报错
s.discard（10） #ok

5.集合运算

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 交集（两个集合都有的）
a & b   # {3, 4}
a.intersection(b)  # {3, 4}
# 并集（合并所有）
a | b   # {1, 2, 3, 4, 5, 6}
a.union(b)  # {1, 2, 3, 4, 5, 6}
# 差集（在a中但不在b中）
a - b   # {1, 2}
a.difference(b)  # {1, 2}
# 对称差集（不同时在a和b中）
a ^ b   # {1, 2, 5, 6}
a.symmetric_difference(b)  # {1, 2, 5, 6}

6.
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)        # {1, 2, 3}
result = list(unique)    # [1, 2, 3]（转回列表）
result = sorted(result)  # 排序
