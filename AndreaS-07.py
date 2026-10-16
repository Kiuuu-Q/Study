1.读取文件
file_object=open('words.txt')
line = file_object.readline()
word = line.strip()      #去除首尾格

for line in open('words.txt'):
    word = line.strip()
    print(word)

2.in运算符
def has_e(word):
    if 'E' in word or 'e' in word:
        return True
    else:
        return False
    #简化：
def has_e(word):
    return 'E'in word or'e'in word

def has_e(word):
    return 'e' in word.lower()    #.lower把所有字母换成小写

3.搜索
def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
