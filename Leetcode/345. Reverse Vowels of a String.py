#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

s = "hello"
vowels = ["a", "e", "i", "o", "u"]

def reverseVowels(str) -> str:
    ss = list(str)
    aux = "x"
    i = 0
    aux_i = 0
    for c in ss:
        if (c == vowels[0] or c == vowels[1] or c == vowels[2] or c == vowels[3] or c == vowels[4]):
            c = ss[aux_i]
            aux = c
            aux_i = i
        i += 1
    return ss
print(reverseVowels(s))