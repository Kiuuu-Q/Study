# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 marks
Define the function func1(D) that receives as a parameter a dictionary
D, in which each key is a positive integer N and the corresponding value
is a list of characters L.
The function returns a list in which each item is a string obtained by repeating
N times each of the characters in L. The list is sorted alphabetically,
in descending order.
For example, if D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'],
the function will return:
L = ['uu', 'ss', 'qqq', 'ee', 'aaa']
'''
def func1(D):
    lst=[]
    for key,value in D.items():
        for x in value:
            lst.append(x*key)
    lst.sort(reverse=True)
    return lst


# %% ----------------------------------- FUNC2------------------------- #
''' func2: 2 marks
Define the function func2(L) that gets as parameter a list L of N lists.
Each list in L can be empty or contain a single list, defined the same way.
The function returns a list of N integers, in which the i-th value
is the number of lists nested in the list at the i-th position in L.
For example, if L = [ [[]], [], [[[]], [[]], [[[[]]]], [], [[[]] ]
the function will return: [1, 0, 2, 1, 3, 0, 2]
'''

def func2(L):
    result = []
    for item in L:
        count = str(item).count('[') - 1
        result.append(count)
    return result


# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 marks
Define the function func3(S) that receives as input a string containing
words separated by commas and, optionally, also by spaces.
The function should extract the words from S, considering only those that
begin with a vowel, and insert them into another list, sorted
alphabetically without considering the difference between uppercase and lowercase.
For example, if S = “Brad,ALIce, keVin, oscar, Dana, UMA,ian, Zoe”
the function will return: ['ALIce', 'ian', 'oscar', 'UMA']
'''

def func3(S):
    lst=[]
    parts=S.replace(","," ").split()
    for word in parts:
        w=word.casefold()
        if w[0] in "aeiou":
            lst.append(word)

    def nocase_lex(string):
        return string.casefold(), string
    return sorted(lst,key=nocase_lex)


#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Define the function `func4(input_filepath, output_filepath)` that reads a file
located at `input_filepath` and writes the identified words to a new file at
`output_filepath`. Words in the input file are separated by various delimiters,
including newlines, spaces, tabs, commas, or semicolons. 

The task is to group these words by their last letter without distinguishing
between uppercase and lowercase letters. Words are considered identical if
they are the same when case is ignored, meaning each word should only be
counted once. 

For each group of words, the output file should include a line formatted as
follows:

`<lowercase letter>: <word count>`

In this format, the initial letter is in lowercase, followed by a colon and a
space. After the colon and space, the number of words ending with that letter
is provided, regardless of the case of the letters in the words. The lines in
the output file should be ordered in descending alphabetical order based on
the letter before the colon.

Please note that there should be no space at the end of each line in the
output file, but each line should end with a carriage return.

The function should return the total number of words in the input file,
including duplicates.
For example:

contents of func4/func4_in1.txt:
GE
wOa;II,see ua;PAO,oA;wOA
pao iu;jJa,kE

By calling the function as:
n = func4(“func4/func4_in1.txt”, “func4/func4_out1.txt”)

the expected contents of func4/func4_out1.txt is:
u: 1
o: 1
i: 1
e: 3
a: 4

and the value of n will be 12
"""

def func4(input_filepath, output_filepath):
    d={}
    count=0
    with open(input_filepath,"r",encoding="utf-8")as f_in:
        lines=f_in.readlines()
        for line in lines:
            line=line.replace(","," ").replace(";"," ").strip().split()
            for word in line:
                count+=1
                word=word.casefold()
                letter=word[-1]
                d.setdefault(letter,set()).add(word)
    sor=sorted(d.items(),reverse=True)
    with open(output_filepath,"w",encoding="utf8")as f_out:
        for letter,word in sor:
            f_out.write(f"{letter}: {len(word)}\n")
    return count








