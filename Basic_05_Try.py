#异常名称
ValueError （ 值错误 ） 
ZeroDivisionError   （除数为0）  
KeyError （字典键不存在）
FileNotFoundError  （文件不存在）
TypeError  （ 类型错误   ）

例子：
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为0"
    except TypeError:
        return "参数必须是数字"
    except:  # 兜底（捕获其他未知异常）
        return "未知错误"
# 测试
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # 除数不能为0
print(safe_divide(10, "a"))  # 参数必须是数字

