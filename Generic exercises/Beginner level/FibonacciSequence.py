#Write a function fib(n) that returns the n-th Fibonacci number. 
#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

def fib(n):
    number1 = 0
    number2 = 1
    for n in range (1, n + 1):
        number3 = number1 + number2
        number1 = number2
        number2 = number3
        i = number3
    return i

#e.g.
a = fib(4)
print(a)