lst = [29,-3,8,-1,1,7,6,2,4]
l = len(lst)

for i in range(l):
    for j in range(i+1,l):
        if lst[i] > lst[j]:
           lst[i],lst[j] = lst[j],lst[i]

print(lst)