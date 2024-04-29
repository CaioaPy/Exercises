#Crie uma função que receba uma lista de números e retorne outra lista contendo apenas os números pares da lista original.
#My code:

def EvenList(numbers):
    pares = []
    for n in numbers:
        n_operacional = n % 2
        if n_operacional == 0:
            pares.append(n)
        else:
            pass
    return pares
listw = [10, 322, 1235, 623, 1267, 235, 6433, 1685, 9245]

EvenNumbers = EvenList(listw)
print(EvenNumbers)