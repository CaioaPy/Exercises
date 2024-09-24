"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
def largestNumber(nums: list[int]) -> str:
    num_list = list(str(nums))
    nums2 = []
    for i in num_list:
        nums2.append(i)
    print(nums2)

nums = 32013201312
largestNumber(nums)