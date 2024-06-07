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
    
for i in range(t):
    if (chars[i] == "I"):
        values.append(I);
    
    elif (chars[i] == 'V'):
        values.append(V);
    
    elif (chars[i] == 'X'):
        values.append(X);
    
    elif (chars[i] == 'L'):
        values.append(L);
    
    elif (chars[i] == 'C'):
        values.append(C);
    
    elif (chars[i] == 'D'):
        values.append(D);
    
    elif (chars[i] == 'M'):
        values.append(M);

i = 0;
while i < t:
    if i + 1 < t and values[i] < values[i + 1]:
        number += values[i + 1] - values[i];
        i += 2;
    else:
        number += values[i];
        i += 1;
print(number)
