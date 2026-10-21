def safe_division(inputfile, outputfile):
    with open(inputfile,"r",encoding="utf-8")as f_in:
        lst=[]
        count=0
        lines=f_in.readlines()
        for line in lines:
            nums=[]     #要在循环里面
            line=line.replace(","," ").split()
            for word in line:
                word=float(word)
                nums.append(word)
            if len(line)<2:
                lst.append("Error")
            elif nums[1]==0:    #逻辑别反了！
                lst.append("Error")
            else:
                res=nums[0]/nums[1]
                lst.append(round(res,3))
                count+=1
    with open(outputfile,"w",encoding="utf-8")as f_out:
        for x in lst:
            f_out.write(str(x)+"\n")
    return count
    pass

def remove_and_reverse(s, index):
    strr=""
    if index>=len(s):
        return s
    else:
        strr+=s[:index]+s[(index+1):]
        
        return strr[::-1]     #字符串一定要用切片
    pass

def list_math(nums):
    even=0
    odd=[]
    if not nums:
        return(0,0)
    else:
        for i in range(len(nums)):
            if i%2==0:
                even+=nums[i]
            else:
                odd.append(nums[i])
    max_odd=max(odd) if odd else 0      #要保证odd存在
    return(even,max_odd)
    pass

def process_words(L0, L1):
    res=[]
    
    for x,y in zip(L0,L1):
        if y>=len(x):             #要加等于号，如果len是3，合法索引就是012，3到下面去会报错
            res.append(x)
        elif y<0:
            res.append(x)
        else:
            big=x[y].upper()      #括号！
            x=x[:y]+big+x[(y+1):]
            res.append(x)
    return(res)
    pass

def filter_and_save(inputfile, outputfile, min_len):
    res=[]
    with open(inputfile,"r",encoding="utf-8")as f_in:
        lines=f_in.readlines()
        for line in lines:
            line=line.replace(',',' ').replace(';',' ').split()
            for word in line:
                if len(word)>=min_len:
                    res.append(word)
    with open(outputfile,"w",encoding="utf-8")as f_out:
        for x in res:
            f_out.write("-".join(x)+"\n")   #会把字母全部拆开
            #"-".join("apple")会变成a-p-p-l-e



#正确做法
def filter_and_save(inputfile, outputfile, min_len):
    all_valid_words = []
    with open(inputfile, "r", encoding="utf-8") as f_in, \
         open(outputfile, "w", encoding="utf-8") as f_out:
        for line in f_in:
            words = line.replace(",", " ").replace(";", " ").split()
            # 提取本行合法的单词
            valid = [w for w in words if len(w) >= min_len]
            #这样写，整一行处理，不会拆散
            all_valid_words.extend(valid)
            
            # 写入对应的行
            f_out.write("-".join(valid) + "\n")
            
    if not all_valid_words:
        return ""
    return min(all_valid_words, key=len)
        








