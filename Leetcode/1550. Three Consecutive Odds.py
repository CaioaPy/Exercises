#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

#e.g.
# Input: arr = [1,2,34,3,4,5,7,23,12]
#Output: true
#Explanation: [5,7,23] are three consecutive odds.

arr = [5, 1, 6, 2, 5, 7, 9, 4, 3, 1]

def threeConsecutiveOdds(nums) -> bool:
    found = False
    n1 = None
    n2 = None
    n3 = None
    for n in nums:
        if n1 == 1 and n2 == 1 and n3 == 1:
            return True
        if n % 2 == 1:
            if n1 == None:
                n1 = 1
            elif n2 == None:
                n2 = 1
            elif n3 == None:
                n3 = 1
        else:
            n1 = None
            n2 = None
            n3 = None
    return False

a = threeConsecutiveOdds(arr)
print(a)