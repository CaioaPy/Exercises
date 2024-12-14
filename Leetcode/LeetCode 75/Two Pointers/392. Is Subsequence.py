#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without
#disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

#Example 1:
#Input: s = "abc", t = "ahbgdc"
#Output: true

#Example 2:
#Input: s = "axc", t = "ahbgdc"
#Output: false

def isSubsequence(s: str, t: str) -> bool:
    s_ind = 0
    t_ind = 0
    while s_ind < len(s) and t_ind < len(t):
        if s[s_ind] == t[t_ind]:
            s_ind += 1
        t_ind += 1
    return s_ind == len(s)

a = "aaawe"
b = "rawasacwe"
x = isSubsequence(a, b)
print(x)