#基本操作
d = {"name": "Tom", "age": 18}
d["name"]        # "Tom"
d.get("gender", "未知")  # "未知"（安全取值）
d["score"] = 90  # 新增/修改
del d["age"]     # 删除
