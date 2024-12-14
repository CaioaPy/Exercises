#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

#Example 2:
#Input: nums = [0]
#Output: [0]

def moveZeroes(nums: list[int]) -> None:
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != non_zero_index:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

a = [1,2,0,8,5,6,0,8,3,0]
print(a)
x = moveZeroes(a)
print(a)