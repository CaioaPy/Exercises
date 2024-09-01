#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


s = "hello"

def reverseVowels(str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    ss = list(str)
    aux = "x"
    i = 0
    aux_i = 0
    for c in ss:
        if (c in vowels):
            c = aux
            aux = c
            aux_i = i
        i += 1

    return ss
print(reverseVowels(s))