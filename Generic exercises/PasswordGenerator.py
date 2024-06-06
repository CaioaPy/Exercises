#Write a Python program to generate a random password of a specified length input by the user. 
#The password should include a mix of uppercase letters, lowercase letters, numbers, and special characters.
import random

elements = ["a"]

def criar(i):
    r = 0
    for r in range(0, i):
        x = random.randint(0, 30)
        password.append(x)
        r += 1


print("welcome to the password generator!")
i = int(input("insert the length for the password: "))
password = []
criar(i)
print(password)
