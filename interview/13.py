lst = [5,-2,4,-2,1]

def max_sum(lst):
    max_dig_sum = lst[0]
    curr_max_sum = lst[0]
    l = len(lst)

    for i in range(1,l):
        curr_max_sum = max(lst[i],curr_max_sum + lst[i])
        max_dig_sum = max(curr_max_sum,max_dig_sum)

        return max_dig_sum


print(max_sum(lst))
