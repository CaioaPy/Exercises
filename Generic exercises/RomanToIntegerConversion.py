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

for i in values:
    print(i, end = " ");
