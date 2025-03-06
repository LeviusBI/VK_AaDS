def twoSum(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        my_sum = nums[i] + nums[j]
        if my_sum < target:
            i += 1
        elif my_sum > target:
            j -= 1
        else:
            return [f'{i}', f'{j}']

twoSum([3, 8, 9, 11, 16, 18, 19, 21], 25)