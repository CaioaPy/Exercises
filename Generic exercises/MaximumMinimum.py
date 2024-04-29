#Find Maximum and Minimum: Write a Python program to find the maximum and minimum numbers in a list.
#My code:

def max_min(numbers):
    lista = []
    lista.extend(numbers)
    lista.sort()
    min_val = lista[0]
    max_val = lista[-1]
    listafinal = []
    listafinal.append(min_val)
    listafinal.append(max_val)
    return listafinal

numeroswww = [3, 2, 5, 1, 2, 6, 12, 4, 23, 521, 342, 54, 2345, 234, 2364]
numeros = max_min(numeroswww)
print(f"The min and max are respective: {numeros}")
