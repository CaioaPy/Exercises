#Objective: Find the missing number in an array of consecutive integers.

#Instructions:

#Create a function find_missing_number(arr: List[int]) -> int that finds the missing number in an array of consecutive integers.

def find_missing_number(List) -> int:
    r = len(List)
    i = List[0]
    for n in List:
        if (n != i):
            return i
        else:
            i += 1

eg = [0,1,2,3,4,6,7,8,9]
print(find_missing_number(eg))