#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#Example 1:
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

#Example 2:
#Input: numRows = 1
#Output: [[1]]

def generate(numRows: int) -> list[list[int]]:
    final = [[1]]
    for currentlen in range(1, numRows):
        row = [1]
        for currentNum in range(1, currentlen):
            row.append(final[currentlen - 1][currentNum - 1] + final[currentlen - 1][currentNum])
        row.append(1)
        final.append(row)
    return final

# test
u = generate(4)
print(u)