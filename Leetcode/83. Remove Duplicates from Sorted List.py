def RemoveDuplicates(nums):
    rang = range(0, len(nums) - 1)
    for n in rang:
        val = nums[n - 1]
        next = nums[n]
        if val == next:
            nums.remove(next)


numeros = [1,2,3,4,4,5,6,7]
print(numeros)
RemoveDuplicates(numeros)
print(numeros)
