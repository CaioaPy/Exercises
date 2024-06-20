#In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket.
#Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that
#the minimum magnetic force between any two balls is maximum.

#Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

#Given the integer array position and the integer m. Return the required force.

# e.g
#Input: position = [1,2,3,4,7], m = 3
#Output: 3

pos = [1, 2, 3, 4, 7, 9]
Ba = 3
def BallsForce(positions, balls) -> int:
    higher = 1
    lower = 1
    for n in positions:
        if n > higher:
            higher = n
        elif n < lower:
            lower = n
    return higher, lower

print(BallsForce(pos, Ba))