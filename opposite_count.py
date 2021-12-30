def opposite_count(nums):
    finalint = 0
    i = 1
    for s in nums:
        while i < len(nums) - 1:
            if s + nums[i] == 0 and nums.index(s) < i:
                finalint += 1
            i += 1
        i = 1
    return finalint
print(opposite_count([ 2, 5, 11, -5, -2, 7 ])) # => 2
print(opposite_count([ 21, -23, 24 -12, 23 ])) # => 6