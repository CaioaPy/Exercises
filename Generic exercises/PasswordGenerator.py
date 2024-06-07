#Write a Python program to generate a random password of a specified length input by the user. 
#The password should include a mix of uppercase letters, lowercase letters, numbers, and special characters.
import random
import string

elements = [char for char in string.ascii_letters + string.digits + "!@#$%&*"]

def criar(i):
    r = 0
    for r in range(0, i):
        x = random.randint(0, 85)
        y = elements[x]
        password.append(y)
        r += 1


print("welcome to the password generator!")
i = int(input("insert the length for the password: "))
password = []
criar(i)
print("".join(password))
