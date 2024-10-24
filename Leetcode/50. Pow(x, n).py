#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

#Example 1:
#Input: x = 2.00000, n = 10
#Output: 1024.00000

#Example 2:
#Input: x = 2.10000, n = 3
#Output: 9.26100

class Solution:
    def myPow(self, x: float, n: int) -> float:
        final = x
        if n == 0 or n < 0:
            return 1
        n -= 1
        while n:
            final *= x
            n -= 1
        return final

x = myPow(2, 5)
print(x)
