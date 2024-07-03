#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it 
#shows in both arrays and you may return the result in any order.

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

lista = [1, 2, 4, 4, 5, 6]
lista2 = [4,5,2]

def SubArray(main_array, subarray) -> list[int]:
    subarray_output = []
    loop = True
    i = 0
    for x in subarray:
        if x in main_array:
            subarray_output.append(x)
    return subarray_output

x = SubArray(lista, lista2)
print(x)