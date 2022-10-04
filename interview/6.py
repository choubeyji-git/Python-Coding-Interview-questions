lst = [5,-2,4,-2,1]

def maxSum(lst):
    max_sum = lst[0]
    curr_max_sum = lst[0]
    l = len(lst)

    for i in range(1,l):
        curr_max_sum = max(lst[i],curr_max_sum + lst[i])
        max_sum = max(max_sum,curr_max_sum)

    return max_sum

print(maxSum(lst))