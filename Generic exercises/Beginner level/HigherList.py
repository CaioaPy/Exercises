#Escreva uma função que recebe uma lista como argumento e retorna o maior número presente na lista.
#My code:

def find_max(numbers):
    numbers.sort()
    return numbers[-1] 

listw = [10, 322, 1235, 623, 1267, 235, 6433, 1685, 9245]

max_number = find_max(listw)
print(max_number)