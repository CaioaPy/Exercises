#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# 5 = 2*2 + 1*1

def checksum(num) -> bool:
    a = 10
    b = 1
    for n in range(1, num):
        c = a*a + b*b
        print(c)
        if (c > num):
            a - 1
            print(c)
        elif (c < num):
            b + 1
            print(c)

print(checksum(5))