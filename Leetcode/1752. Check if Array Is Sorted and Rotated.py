#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise,
#return false.

#There may be duplicates in the original array.

#Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

nums = [3,4,5,1,2]

def check(lista) -> bool:
    sorted_nums = sorted(lista)
    x = 0
    i = 0
    leng = len(lista)
    print(sorted_nums)
    for i in range(0, leng):
        if sorted_nums[i] == lista[0]:
            x = i
    if x != 0:
        print(x)
        return True
    else:
        return False

print(check(nums))