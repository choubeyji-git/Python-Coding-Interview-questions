# Input = [5,-2,4,-2,1]

# Output: 7

lst = [5,-2,4,-2,1]

def maxSum(lst):
    l = len(lst)
    max_sum = lst[0]
    curr_max_sum = lst[0]

    for i in range(1,l):
        curr_max_sum = max(lst[i],curr_max_sum + lst[i])
        max_sum = max(max_sum,curr_max_sum)

    print(max_sum)

maxSum(lst)
