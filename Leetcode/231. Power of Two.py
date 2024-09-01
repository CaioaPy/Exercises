#231. Power of Two
#Given an integer n, return true if it is a power of two. Otherwise, return false.
#An integer n is a power of two, if there exists an integer x such that n == 2x.

def PowerofTwo(n) -> bool:
    I = True
    y = 0
    while I:
        x = 2 ** y
        if n == x:
            return True
        elif n < x:
            return False
        y += 1
        
