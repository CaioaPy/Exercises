#List Manipulation:
##Write a Python program to:
##Create a list of integers from user input
##Print the sum of the elements in the list
##Print the maximum and minimum elements in the list
##Sort the list in ascending order
##Reverse the list
###My Code:

def create_list():
    integer_list = []
    numbers = int(input("insert the number of integers you want to add to the list: "))
    print("enter the integers:")
    for n in range(numbers):
        num = int(input())
        integer_list.append(num)
    return integer_list

def sum_list(lista):
    soma = sum(lista)
    return soma

def Max_Min_List(lista):
    lista.sort()
    max = lista[-1]
    min = lista[0]
    MaxMin = []
    MaxMin.append(min)
    MaxMin.append(max)
    return MaxMin

def Sort_List(lista):
    lista.sort()
    return lista

def Reverse_list(lista):
    lista.reverse()
    return lista
