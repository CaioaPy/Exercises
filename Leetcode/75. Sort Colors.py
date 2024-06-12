#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

nums = [2,0,2,1,1,0]
red = []
white = [] 
blue = []
for n in nums:
    if n == 0:
        red.append(0)
    elif n == 1:
        white.append(1)
    elif n == 2:
        blue.append(2)
