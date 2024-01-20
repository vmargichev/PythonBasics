def find_max(nums):
    max_so_far = float("-inf")
    if len(nums) == 0:
        return max_so_far
    else:
        max = nums[0]
        for num in nums:
            if num > max:
                max = num
        return max