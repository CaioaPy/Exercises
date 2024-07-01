#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

#e.g.
# Input: arr = [1,2,34,3,4,5,7,23,12]
#Output: true
#Explanation: [5,7,23] are three consecutive odds.

arr = [5, 1, 6, 2, 5, 7, 9, 4, 3, 1]

def threeConsecutiveOdds(nums) -> bool:
    