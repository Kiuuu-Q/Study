1.交换AB值
if A>B:
  A,B=B,A
 
2.新写法
answer+=[X]
answer.append(X)


3.乘法表
def mult_table(N):
    for x in range(1,N+1):
        for y in range(1,N+1):
             print(x*y,end=' ')。  #默认的end是'\n'，这样可以避免换行
        print()     #换行



4.ASCII码加密解密
def encode_char(C,K):
  code=ord(C)  #将字母转为数字码
  moved=code+K #将ASCII码加上位移量K，得到新码
  return chr(moved) #转回字符
    #比如说输入A，K=2.那么最后会得到C

     #上一版使用的是65-90的ASCII码，90+2就会乱码，所以要优化
def encode_char(C,K):
  code=ord(C)-ord('A')     #ord（‘A’）是65，这样A就变成了0，B变成1……
  moved=(code+K)%26+ord('A')     #无论数字多大都可以弄回[0,25]
  return chr(moved)

     #加密
def cesar_encrypy(text,K):
    text=text.upper()   #都转换成大写，方便
    encrypted=""
    for character in text:
        if'A'<=character<='Z':    #如果在26个字母范围内
            encoded=encode_char(character,K)       #解码
            encrypted+=encoded       #拼接，比如ACBD
        else:
            encrypted+=character       #如果不是字母，就直接加上去
    return encrypted


     #解密
def caesar_decrypt(text,K):
    return caesar_encrypt(text,-K)
        #加密的过程：把字母在字母表右移K位，
         解密的过程：左移K位。
         所以，-K就是反着走，解密


5.进制转换
       #前置函数
def convert_digit(letter):
    if '0'<=letter<='9':
        return int(letter)
    elif 'A'<=letter<='Z':
        return 10+ord(letter)-ord('A')       #用相对于A的偏移来算出。比如F是16，A是10
    else:
        return 0

      #真正开始转换
def convert_base(X,K):      #K是进制
    current_sum=0
    current_power=1  #当前权重
    for letter in reversed(text):    #reversed倒过来，比如ABC变CBA，因为要从低位开始
        number=convert_digit(letter)     #比如说16进制的1F，F换过来number就是15
        contribution=current_power*number
        current_sum+=contribution
        current_power*=K
    return current_sum














