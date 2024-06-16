#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

s = "hello"
ss = list(s)
vowels = ["a", "e", "i", "o", "u"]

def reverseVowels(str) -> str:
    aux = "x"
    i = 0
    aux_i = 0
    for c in str:
        if (aux in vowels):
            ss[aux_i] = aux
            print("a")

        if (c == vowels):
            aux = c
            aux_i = i
        i += 1
    return ss
print(reverseVowels(ss))