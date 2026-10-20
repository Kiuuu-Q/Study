import re


1.
s = "hello world"

re.match(r"world", s)      # None —— match 必须从索引0开始算
re.search(r"world", s)     # <Match 'world'>
re.fullmatch(r"hello", s)  # None —— 必须匹配整串
re.fullmatch(r"hello.*", s) # <Match 'hello world'>—— 有hello就行



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
pattern = 'Mina|Murray'

result = find_first(pattern)
result.string
# 'CHAPTER V. Letters—Lucy and Mina\n'
count_matches('Mina|Murray')   # 229
#| 左边或右边任意一个匹配即可。 count_matches 数出有 229 行提到她（名或姓）
