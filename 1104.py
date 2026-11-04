#处理字典
sen='how are you how do you do do you you'
words=sen.split()     
            #变成words = ['how', 'are', 'you', 'how', 'do', 'you', 'do', 'do', 'you', 'you']
d={}
for word in words:
    d[word]=d.get(word,0)+1      #{'how': 1}一直往里面加
    # if word in frq_dict:
    #     d[word]+=1
    # else:
    #     d[word]=1
for key,value in sorted(frq_dict.items(),key=lambda x:x[1],reverse=True):
    print(key,value)
        #.items变成[('how', 2), ('are', 1), ('you', 4), ('do', 3)]//x:x[1]意思是看数字
