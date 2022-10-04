# lst = [1,2,3,1]
# Output: 4


nums = [4,3,5,10]
len_nums = len(nums)

max_sum = []

for i in nums:
    if nums.index(i) != (nums.index(max(nums)) and nums.index(max(nums))-1) and nums.index(max(nums)) and (nums.index(i) != (nums.index(i) +1)) and (nums.index(i) != nums.index(max(nums))):
        max_sum.append(i+max(nums))

print(max(max_sum))
