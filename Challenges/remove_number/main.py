def remove_nonints(nums):
    nums_filter = []
    for num in nums:
        if type(num) == int:
            nums_filter.append(num)
    return nums_filter