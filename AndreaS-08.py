import re


1.
s = "hello world"

re.match(r"world", s)      # None —— match 必须从索引0开始算
re.search(r"world", s)     # <Match 'world'>
re.fullmatch(r"hello", s)  # None —— 必须匹配整串
re.fullmatch(r"hello.*", s) # <Match 'hello world'>—— 有hello就行

    #我们可以使用这个函数找到第1次提到某个角色的行。
def find_first(pattern):
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            return result



2.
text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."
pattern = 'Dracula'

result = re.search(pattern, text)
result          # <re.Match object; span=(5, 12), match='Dracula'>
result.string   # 'I am Dracula; and I bid you welcome...'
result.group()  # 'Dracula'
result.span()   # (5, 12)

    #数一下出现了几次
def count_matches(pattern):
    count = 0
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            count += 1
    return count



3.

     #左右任意一个就可以
pattern = 'Mina|Murray'

     # 以 Dracula 开头的行
result = find_first('^Dracula')   

    # 以 Harker 结尾的行
result = find_first('Harker$')

    # 匹配 center 或 centre
pattern = 'cent(er|re)' 

    # colour 或 color
pattern = 'colou?r'


4.findall
 
re.findall(r"\d+", "a1 bb22")                     # ['1', '22']
re.findall(r"(\d+)px", "10px 20px 30em")          # ['10', '20'] 
re.findall(r"(\w+)=(\d+)", "a=1,b=2")            # [('a', '1'), ('b', '2')]
re.findall(r"(?:\d+)px", "10px 20px")          # ['10px', '20px'] 
re.findall(r"[a-z]+", "Hello World", re.I)      # ['Hello', 'World']   ← re.I 让 [a-z] 也匹配大写

5.finditer


6.strip
"xxhelloxx".strip("x")          # 'hello'    ← 去掉首尾所有的 'x'
"###title###".strip("#")       # 'title'






















