#Write a Python program to calculate the sum of all numbers from 1 to n using a for loop.
#My code:

def sum_to_n(n):
    m = 0
    for i in range(1, n + 1):
        m += i
    return m

x = sum_to_n(3)
print(x)