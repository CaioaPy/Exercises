#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#Example 1:
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

#Example 2:
#Input: numRows = 1
#Output: [[1]]

def generate(numRows: int) -> list[list[int]]:
    final = [[]]
    final[[1]] = 1
    while numRows:
        currentlen = len(final)
        while currentlen:
            nums = currentlen / 2
            nums = round(nums)
            currentNum = 0
            while nums:
                row = []
                if currentNum == 0 or currentNum == currentlen - 1:
                    row.append(1)
                else:
                    

#test
a = [[2], [2]]
x = len(a)
y = 3 / 2
print(x)
print(y)