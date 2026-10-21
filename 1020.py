#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py 
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER
 3) When your functions are ready, save the file in the window for the
    collection.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "HUIQIAO"
surname = "DENG"
student_id = "202621350171"



# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 20 marks
Define the function func1(int_list, n, outputfilename) that takes as its
input a list of integers int_list, an integer n, and a string outputfilename.
The function must write in a new file named outputfilename all the
reminders of the division by n of all the integers in int_list, 
separated by a single whitespace. 
The reminders must be written in ascending order.

Moreover, the function must return the number of integers in int_list with a
remainder of 0 when divided by n.

Example:
    func1([16, 14, 10, 4, 2, 1, 12], 7) should return 1 and write the
    following line in outputfilename:
0 1 2 2 3 4 5

'''
def func1(int_list, n, outputfilename):
    lst=[]
    count=0
    for x in int_list:
        y=x%n
        lst.append(y)
        if y==0:
            count+=1
    new_list=sorted(lst)
    with open(outputfilename,"w",encoding="utf-8")as f:
        f.write(" ".join(str(x)for x in new_list))
    return count
        
    
    
    
    pass


# print(func1([16, 14, 10, 4, 2, 1, 12], 7, 'func1/out01.txt'))

# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 20 marks
Define the function func2(filename) that receives a string representing
the name of a file. The file contains several words separated by spaces,
commas, and semicolons. The function must find all the words representing
an turn the maximum ininteger number and reteger found.
'''
def func2(namefile):
    lst=[]
    with open(namefile,"r",encoding="utf-8")as f:
        lines=f.readlines()
        for line in lines:
            line=line.replace(",", " ").replace(";", " ").split()
            for word in line:
                if word.isdigit():
                    lst.append(int(word))
    max_num=max(lst)
    return max_num
            
    
    
    pass

# print(func2('func2/in01.txt'))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 20 marks
Define a function func3(L0, L1) that receives 2 lists L0 and L1.
The first list L0 contains strings S0, S1, ... Sn-1, the second list L1
contains positive integers I0, I1, ... In-1.
For each string in Si in L0, the function must remove the character in
position Ii. The function returns the string obtained by concatenating all the
strings with the removed character.
If Ij is an index outside the length of the string, the function does not
remove any character.
For example, if L0 = ['ab', 'qwerty', 'o o'] and L1 = [1, 2, 3] the function
returns: 'aqwrtyo o'.
In facts: 'ab'[1] -> b, 'qwerty'[2] -> e, 'o o'[3] does not exist.
'''

def func3(L0, L1):
    strr=''
    for x,y in zip(L0,L1):
        y=int(y)
        if y<len(x):
            strr+=x[:y]+x[(y+1):]
        else:
            strr+=x
       
    return strr
        
        
    
    pass

# print(func3(['ab', 'qwerty', 'o o'], [1, 2, 3])) 

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 40 marks
Define a function func4(inputfilename, outputfilename) that receives two
strings representing the names of files.

The function must read the file named inputfilename and write to
a new file named outputfilename.
The file inputfilename contains several lines with numbers (float or int)
separated by commas or semicolons and optionally by zero or more whitespaces.
For each line of the input file, the function must write the corresponding
line of the output file with the division of the maximum of all the
numbers in even positions by the minimum of all the numbers in odd positions,
rounded to the second decimal digit.
Positions start from 0 (an even number). If the minimum number of all the 
numbers in even positions is 0, the function must write a 0.

The function must return the minimum value written in the file.

For example, if the first line of inputfilename contains the following line

100,20;30,39.5,50; 0.5

the first line written by the function must be
200.0
        
"""

def func4(inputfilename, outputfilename):
    s=[]
    with open(inputfilename,"r",encoding="utf-8")as f_in:
        lines=f_in.readlines()
        for line in lines:
            odd=[]
            even=[]
            line=line.replace(",", " ").replace(";", " ").split()
            nums=[float(x) for x in line]     #line本来是字符串，要变成浮点数
            for i in range(0,len(nums)):
                if i%2==0:
                    even.append(nums[i])
                else:
                    odd.append(nums[i])
            if not odd or not even:
                d=0.0
            elif min(odd)==0:
                d=0.0
            else:
                max_num=max(even)
                min_num=min(odd)
                d=max_num/min_num
            s.append(round(d,2))
            odd.clear()
            even.clear()
           
  
    with open(outputfilename,"w",encoding="utf-8")as f_out:
        for x in s:
            f_out.write((str(x))+"\n")
       
    return min(s) if s else 0.0
    
            
                 

            
          
        
   
        
        
        
        
        
       
                 
        
        
        
        
        
        
        
    pass


###########################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
