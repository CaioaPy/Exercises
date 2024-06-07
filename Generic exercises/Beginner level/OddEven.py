#Escreva um programa que peça ao usuário para inserir um número e então imprima se o número é par ou ímpar.
#My code:

num = input("Input your number: \n")
num = num % 2
if num == 0:
    print("Even number!")
else:
    print("Odd number!")