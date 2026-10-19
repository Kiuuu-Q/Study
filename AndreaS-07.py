1.文件
file_object=open('words.txt')
line = file_object.readline()
word = line.strip()      #去除首尾格
word=line.replace(',',' ')

for line in open('words.txt'):
    word = line.strip()
    print(word)

output_file.write('Andrea')
output_file.close()    #不写的话会丢失文件


 
f.write(f"{x*y}" ）
print(x*y,end=" ",file=output_file)



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
        else:
            return False













