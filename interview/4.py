# Given an array of both positive and negative numbers, find out the largest sum that can be achieved by considering any-one subarray of the given array
# Input = [5,-2,4,-2,1]
# Output: 7


def largestSum(nums):
    max_so_far = nums[0]
    curr_max = nums[0]
    l = len(nums)
    for i in range(1,l):
        curr_max = max(nums[i],curr_max + nums[i])
        max_so_far = max(max_so_far,curr_max)
    
    return max_so_far 

print(largestSum([5,-2,4,-2,1]))    

