a = [1, 2, 3, 4, 5, 10]
b = [2, 3, 1, 0, 5]

def notInlst(a,b):
    opLst = [i for i in a if i not in b]
    return opLst

print(notInlst(a,b))
