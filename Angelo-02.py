def matrix_sum(A, B):
    # 检查行数是否相同
    if len(A) != len(B):
        return False

    C = []
    for rowA, rowB in zip(A, B):
        # 检查对应行的长度是否相同
        if len(rowA) != len(rowB):
            return False

        newrow = []
        for a, b in zip(rowA, rowB):
            newrow.append(a + b)
        C.append(newrow)

    return C



def rem_consec_dupl(alist):
    count = 0
    i = 0

    while i < len(alist) - 1:
        if alist[i] == alist[i + 1]:
            alist.pop(i + 1)
            count += 1
        else:
            i += 1

    return count


def nor(d):
    new_d = {}
    for key, value in d.items():
                    # 这里用 title() 让每个单词首字母都大写（capitalize是第一个）
        new_key = key.strip().title() 
        new_value = value.strip().upper()
        new_d[new_key] = new_value
    return new_d

d = {' angelo spognardi ': ' admin ', 'xi zhang': ' editor', 'guo li zhu': 'guest '}
print(nor(d))
# 输出完美匹配目标：{'Angelo Spognardi': 'ADMIN', 'Xi Zhang': 'EDITOR', 'Guo Li Zhu': 'GUEST'}
