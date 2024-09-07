#You are given an array of integers nums and the head of a linked list. 
#Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

#Example 1:

#Input: nums = [1,2,3], head = [1,2,3,4,5]

#Output: [4,5]

def modifiedList(nums: list[int], head: list[int]) -> list[int]:
    for i in nums:
        if i in head:
            nums.remove(i)
    print(nums)

we = [1,2,3,4,5]
aw = [1,2]

modifiedList(we, aw)