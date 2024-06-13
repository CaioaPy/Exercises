#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

s = "hello"
vowels = ["a", "e", "i", "o", "u"]

def reverseVowels(str) -> str:
    for c in str:
        if c