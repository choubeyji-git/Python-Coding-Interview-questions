arr = [2,4,1,8,3,5,1,3]
k = 3

l = [i for i in arr if arr.count(i) ==1]

print(l)

if len(l) > k:
    l.pop(len(l)-k)

print(l)