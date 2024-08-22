# without the in place O(1)
def reverter(palavra):
    holder = ""
    index = len(palavra)
    while index:
        index -= 1
        holder += palavra[index]
    return holder

a = "agua"
print(a)
b = reverter(a)
print(b)

#using the in place
def reverter(palavra):
    holder = ""
    index = len(palavra)
    while index:
        index -= 1
        holder += palavra[index]
        print(palavra)
        palavra[:-index]
    palavra = holder
    return palavra


a = "agua"
print(a)
b = reverter(a)
print(b)
