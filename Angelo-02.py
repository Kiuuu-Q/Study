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
