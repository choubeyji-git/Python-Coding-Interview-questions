# Input: nums = [3,7,11,15], target = 14
# Output: [0,2]


def index_sum(ele,target):
    op = []
    l = len(ele)
    for i in range(l):
        for j in range(i+1,l):
            if ele[i] + ele[j] == target:
                op.append(ele.index(ele[i]))
                op.append(ele.index(ele[j]))
    print(op)


index_sum([3,7,11,15],14)