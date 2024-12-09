#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#Example 1:
#Input: s = "IceCreAm"
#Output: "AceCreIm"
#Explanation:
#The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

#Example 2:
#Input: s = "leetcode"
#Output: "leotcede"

def reverseVowels(s: str) -> str:
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    i = 0
    vowels_in_word = []
    for c in s:
        if c in vowels:
            vowels_in_word.append(i)
        i += 1
    final_string = ""
    ind = -1
    for l in s:
        if l in vowels:
            aux = vowels_in_word[ind]
            aux = s[aux]
            final_string += aux
            ind -= 1
        else:
            final_string += l
    return final_string


x = reverseVowels("minecraft")
print(x)