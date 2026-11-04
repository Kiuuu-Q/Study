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





'''
Write a function that checks if a player is able to craft an item by assembling
it from the materials in their inventory.
Return True if every material required in the recipe is present in the inventory
in sufficient quantity (greater than or equal).
If a recipe material does not exist or is insufficient in the inventory, the result is False.

The inventory is a list containing the names of each unit of available material.
The recipe is a dictionary in the format 'material': quantity.

Example 1:
inventory: ['iron', 'wood', 'paper', 'iron', 'iron', 'wood', 'wood']
recipe: {'iron': 3, 'leather': 1}
Result: False (leather is missing from the inventory)

Example 2:
inventory: ['iron', 'wood', 'paper', 'iron', 'iron', 'wood', 'wood']
recipe: {'iron': 2, 'wood': 4}
Result: False (available wood is 3, required wood is 4)'''

def number_of_craftable(inventory: list, recipe: dict): -> int:
    # 第一步：用字典统计配方里需要的每种材料在背包里有多少个
    invdict = {m: inventory.count(m) for m in recipe}
    
    # 第二步：准备一个空列表，用来装每种材料能合成的数量
    craftable = []
    for m, quant in recipe.items():
        # 计算当前材料能造几个 (数量 // 配方需求)，并加入列表
        craftable.append(invdict[m] // quant)
        
    # 第三步：挑出列表里最小的那个数字（木桶短板），就是最终能造出的总数
    return min(craftable)



def number_of_craftable(inventory: list, recipe: dict) -> int:
    # 记录最小能造几个，一开始设一个很大的数（比如 999）
    min_craft = 9999  
    for key, value in recipe.items():
        num = inventory.count(key)  # 背包里有几个
        can_make = num // value     # 能造几个（// 是整除，比如 3 // 2 得 1）
        
        # 如果这个材料能造的数量，比目前记录的最小值还要小，就更新最小值
        if can_make < min_craft:
            min_craft = can_make
        
    return min_craft












