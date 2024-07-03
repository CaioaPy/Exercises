#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it 
#shows in both arrays and you may return the result in any order.

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

def SubArray(main_array, subarray) -> list[int]:
    loop = False
    i = 0
    subarray_output = []
    while loop:
        x = subarray[i]
        for n in main_array:
            if n == x:
                subarray_output.append(n)
        i += 1
        if len(subarray_output) == len(subarray):
            loop = False
    return subarray_output
