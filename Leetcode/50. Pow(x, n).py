#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

#Example 1:
#Input: x = 2.00000, n = 10
#Output: 1024.00000

#Example 2:
#Input: x = 2.10000, n = 3
#Output: 9.26100


def myPow(x: float, n: int) -> float:
    final = x
    n -= 1
    while n:
        final *= x
        n -= 1
    return final

#test
x = myPow(2, 3)
print(x)
