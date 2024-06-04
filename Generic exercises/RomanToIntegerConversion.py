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
    
for i in range(t):
    if (chars[i] == "I"):
        values[i] += I;
    
    elif (chars[i] == 'V'):
        values[i] += V;
    
    elif (chars[i] == 'X'):
        values[i] += X;
    
    elif (chars[i] == 'L'):
        values[i] += L;
    
    elif (chars[i] == 'C'):
        values[i] += C;
    
    elif (chars[i] == 'D'):
        values[i] += D;
    
    elif (chars[i] == 'M'):
        values[i] += M;

#test only
for i in values:
    print(i, end = " ");
#test only

loop = 0;
Loopi = 0;
while loop < t:
    x1 = values[Loopi]
    Loopi += 1;
    x2 = values[Loopi]
    if (x1 < x2):
        x3 = x2 - x1;
        number += x3;
    else:
        number += x1;
    loop += 1;
print(number)
