 #交换AB值
if A>B:
  A,B=B,A
 
#新写法
answer+=[X]
answer.append(X)


#ASCII码
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
