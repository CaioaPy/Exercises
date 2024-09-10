#You are given two integers m and n, which represent the dimensions of a matrix.
#You are also given the head of a linked list of integers.
#Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
#Return the generated matrix.

#Example 1:
#Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
#Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
#Explanation: The diagram above shows how the values are printed in the matrix.
#Note that the remaining spaces in the matrix are filled with -1.

def spiralMatrix(m: int, n: int):
    final_array = [[-1] * m] * n
    create = 0
    up = False
    back = False
    arr = [1,2,3,4,5,6,7]
    x = 0
    indo = True
    descecndo = True
    while create < len(arr):
        if (indo):
            for i in range (0, n):
                final_array[i][0] = arr[x]
        if (descecndo):
            for i in range (0, m):
                final_array = arr[x]
        x += 1
spiralMatrix(2, 4)
