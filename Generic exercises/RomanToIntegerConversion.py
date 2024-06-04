#Roman to Integer Conversion

I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;

numberInStr = input("insert the number in roman numerals: \n");
number = 0;
chars = list(numberInStr);
values = []
t = len(chars)
for n in range(t):
    values.append(0);


"""
for i in numberInStr:
    if (chars[i] == "I"):
        number += I;
    
    elif (chars[i] == 'V'):
        number += V;
    
    elif (chars[i] == 'X'):
        number += X;
    
    elif (chars[i] == 'L'):
        number += L;
    
    elif (chars[i] == 'C'):
        number += C
    
    elif (chars[i] == 'D'):
        number += D
    
    elif (chars[i] == 'M'):
        number += M
"""
