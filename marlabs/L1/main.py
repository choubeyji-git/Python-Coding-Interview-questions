lst = [1,1,1,1,2,3,6,7,8,8,8,8]

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

lst = []

for k,v in d.items():
    if v != 1:
        lst.append(k)

print(lst)