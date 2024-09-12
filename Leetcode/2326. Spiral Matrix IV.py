#You are given two integers m and n, which represent the dimensions of a matrix.
#You are also given the head of a linked list of integers.
#Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
#Return the generated matrix.

#Example 1:
#Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
#Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
#Explanation: The diagram above shows how the values are printed in the matrix.
#Note that the remaining spaces in the matrix are filled with -1.

def spiralMatrix(m: int, n: int, arr):
    final_array = [[-1] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    D_index = 0  
    row, col = 0, 0 
    index = 0  

    while index < len(arr):
        final_array[row][col] = arr[index]
        index += 1 
        
        next_row = row + directions[D_index][0]
        next_col = col + directions[D_index][1]

        if 0 <= next_row < m and 0 <= next_col < n and final_array[next_row][next_col] == -1:
            row, col = next_row, next_col
        else:
            D_index = (D_index + 1) % 4
            row += directions[D_index][0]
            col += directions[D_index][1]
    for row in final_array:
        print(row)

awe = [1, 2, 3, 4, 5, 6]
spiralMatrix(4, 4, awe)