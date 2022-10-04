lst = [29,-3,8,-1,1,7,6,2,4]
after_sort = []

while lst:
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    after_sort.append(minimum)
    lst.remove(minimum)


print(after_sort)
