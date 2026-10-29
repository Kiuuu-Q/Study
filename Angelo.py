排序方法

1.casefold忽略大小写

# To order a list of string ignoring the case and
# then in alphabetical order
def nocase_lex(string):
    return string.casefold(), string

#这样会返回一个元组，比如('abc', 'Abc')。sorted() 比较元组时，会依次比较其中的元素：
先比较 string.casefold()：忽略大小写，按字母顺序排列。
如果第一项相同，再比较原字符串：按字符的 Unicode 编码顺序排列。对于英文字母，大写排在小写前面。

p= ['Abc', 'abC', 'AbC', 'abc', 'acb', 'ACb', 'CAB', 'cAb']
print(sorted(p, key =  nocase_lex))



2.

# Define a key function for sorting tuples of three elements, 
# considering the second element first, then the third, then the first
def change_order(tup):
    return tup[1], tup[2], tup[0]      #先看第二个，再看第三个，最后看第一个

def change_order(tup):
    a,b,c = tup
    return b, c, a
    
l = [(1,5,6), (3,4,9), (1,1,1)]     #变成(5, 6, 1)
sorted(l, key = change_order) # [(1,1,1), (3,4,9), (1,5,6)]



3.
# Define a key function for sorting a list of strings, considering
# the number of characters in increasing order, then the ending letter,
# then the alphabetical order

def len_end_alpha(string):
    return len(string), string[-1], string      #先按字符串长度，再按最后一个字母，最后按整个字符串的字母顺序，都采用升序。
    
l = ['snake', 'caterpillar', 'rat', 'bat', 'dog']     #(5, 'e', 'snake')
print(sorted(l, key = len_end_alpha)) # ['dog', 'bat','rat', 'snake', 'caterpillar'])




4.
# Define a key function for sorting a list of strings, considering
# the number of vowels in decreasing order, then the length in increasing,
# order, then the reverse alphabetical order.

def vowels_len_alpha(string):
    count = 0
    for char in string:
        if char in 'aeiouy':
            count+=1
    return count, -len(string), string     #元音数量降序 → 字符串长度升序 → 字符串逆字母顺序（reverse=True）
    
l= ['pear', 'peach', 'apple', 'banana', 'avocado'] 
print(sorted(l, key = vowels_len_alpha, reverse = True)) # ['avocado', 'banana', 'pear', 'peach', 'apple']









    
