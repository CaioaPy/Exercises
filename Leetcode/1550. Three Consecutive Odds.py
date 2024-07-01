#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

#e.g.
# Input: arr = [1,2,34,3,4,5,7,23,12]
#Output: true
#Explanation: [5,7,23] are three consecutive odds.

arr = [1, 1, 1]

def threeConsecutiveOdds(nums) -> bool:
    n1 = None
    n2 = None
    n3 = None
    for n in nums:
        if n1 == 1 and n2 == 1 and n3 == 1:
            return True
        elif n % 2 == 1 or n == 1:
            if n1 == None:
                n1 = 1
            elif n2 == None:
                n2 = 1
            elif n3 == None:
                n3 = 1
        elif n % 2 == 0:
            n1 = None
            n2 = None
            n3 = None
    if n1 == 1 and n2 == 1 and n3 == 1:
        return True
    else:
        return False

a = threeConsecutiveOdds(arr)
print(a)