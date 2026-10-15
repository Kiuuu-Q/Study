import time

1. 获取当前时间戳：time.time()
时间戳是从 Unix 纪元（1970 年 1 月 1 日 00:00:00 UTC）至今经过的秒数。
now = time.time()
print(now)       # 浮点数，包含小数秒
print(int(now))  # 整数秒

2. 让程序暂停：time.sleep()
参数单位为秒，也可以使用小数：
print("开始")
time.sleep(2)     # 暂停约 2 秒
print("结束")
time.sleep(0.5)   # 暂停约半秒

3. 转换为本地时间：time.localtime()
它把时间戳转换为包含年、月、日、时、分、秒等信息的 struct_time 对象：
t = time.localtime()  # 不传参数时，使用当前时间
print(t.tm_year)      # 年
print(t.tm_mon)       # 月，1～12
print(t.tm_mday)      # 日，1～31
print(t.tm_hour)      # 小时，0～23

4. 把时间显示为字符串：time.strftime()
t = time.localtime()
text = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(text)  # 例如：2026-10-15 14:30:05
