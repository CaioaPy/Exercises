#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise,
#return false.

#There may be duplicates in the original array.

#Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

nums = [3,4,5,1,2]

def check(nums) -> bool:
    sorted_nums = nums.sort()
    i = 0
    x = 0
    for n in sorted_nums:
        i += 1
        if n == nums[i]:
            x = i
    print(x)