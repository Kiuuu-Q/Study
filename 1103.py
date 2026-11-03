'''func1: 20 marks

Write a function func1(L) that receives as input:
- L: a list of lists of integers.

The function returns a set containing the numbers that appear
in all of the lists in L.

Example:
L = [[4, 2, 6], [6, 3, 6], [2, 1, 6]]
func1(L)
output: {6}
'''

def func1(L):
    result = set(L[0])
    for lst in L[1:]:
        result &= set(lst)          # 集合交集
    return result


    pass


#类似
写一个函数 common_keys(dicts)，输入是一个列表，元素是字典（每个字典的键是字符串，值是整数）。
函数返回一个集合，包含所有字典中都出现过的键。
def common_keys(dicts):
    result = set(dicts[0])    #set（dict）取的是键    
    for d in dicts[1:]:
        result &= set(d)          
        if not result:         
            break
    return result



# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 20 marks

Write a function func2(words) that receives as input:
- words: a list of strings.

The function returns a dictionary where:
- each key is an integer N,
- the corresponding value is a list of words from the input that have that
  have exactly N unique characters; the list is sorted in ascending alphabetical order.

Example:
words = ['apple', 'pear', 'banana', 'tea', 'dog', 'ant']
func2(words)
output: {4: ['apple', 'pear'], 3: ['ant', 'banana', 'dog', 'tea']}
'''

def func2(words):
    dic={}
    for word in words:
        n=len(set(word))
        dic.setdefault(n,[]).append(word)
        for lst in dic.values():
            lst.sort()
    return dic


    pass
# %% ----------------------------------- FUNC3 ------------------------- #
'''func3: 20 marks

Write a function func3(int_list, Action) that receives as input:
- int_list: a list of integer values.
- Action: a dictionary with integer keys and values that are either 'a' (add) or 'r' (remove).

The function must modify the input list in place so that:
- For every key in Action:
    - If Action[value] is 'a', then value must be appended to the list;
    - If Action[value] is 'r', then all occurrences of value must be removed from the list.
Finally, the list must be sorted in descending order.
The function returns the number of elements removed from int_list.

Example:
int_list = [7, 3, 6, 5, 7]
Action = {2: 'a', 7: 'r', 4: 'a'}
func3(int_list, Action) returns 2 and after the calling, int_list is [6, 5, 4, 3, 2]
'''

def func3(int_list, Action):
    count=0
    for key,value in Action.items():
        if value=="r":
            count+=int_list.count(key)
            int_list[:]=[x for x in int_list if x!=key ]
        elif value=="a":
            int_list.append(int(key))
    int_list.sort(reverse=True)
    return count
    pass

# %% ----------------------------------- FUNC4 ------------------------- #
'''func4: 20 marks

Write a function func4(pairs) that receives as input:
- pairs: a set of tuples, each of the form (int, string)

The function returns a list of pairs, sorted:

- by string length, descending;
- in case of a tie, by the string value, ascending;
- in case of a tie, by the int value, descending.

Note: to sort the list, you must use the key parameter in the sorted function
    and write an explicit key function using all elements of each triple.

Example:
pairs = {
    (2, "cat"),
    (2, "fish"),
    (1, "cat"),
    (2, "bat")
}
func4(pairs)
# output: [(2, "fish"), (2, "bat"), (2, "cat"), (1, "cat")]
'''

def func4(pairs):
    def key_func(pair):
        n,s=pair
        return(-len(s),s,-n)
    return sorted(pairs,key=key_func)

    pass


























