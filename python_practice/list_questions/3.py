# sort a list without using sort keyword

lst = [21,2,-1,8,1,4,3]

n = len(lst)

for i in range(n):
    for j in range(i+1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]


print(lst)