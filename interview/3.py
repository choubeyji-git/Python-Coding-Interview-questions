# Input: nums = [3,7,11,15], target = 14
# Output: [0,2]

def sumOfNums(nums,target):
    l = len(nums)
    op = []
    for i in range(l):
        for j in range(i+1,l):
            if nums[i] + nums[j] == target:
                op.append(nums.index(nums[i]))
                op.append(nums.index(nums[j]))

    return op

print(sumOfNums([3,7,11,15],14))


