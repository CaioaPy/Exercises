#In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket.
#Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that
#the minimum magnetic force between any two balls is maximum.

#Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

#Given the integer array position and the integer m. Return the required force.

# e.g
#Input: position = [1,2,3,4,7], m = 3
#Output: 3

pos = [1, 2, 3, 4, 7]
Ba = 3


def discheck(positions, dis, balls) -> bool:
    first = positions[0]
    count = 1
    for n in positions[1:]:
        if n - first >= dis:
            count += 1
            first = n
            if count >= balls:
                return True
    return count >= balls

def BallsForce(positions, balls) -> int:
    positions.sort()
    lower = 0
    higher = positions[-1] - positions[0]
    while (lower < higher):
        dis = (higher + lower) // 2
        if discheck(positions, dis, balls):
            lower = dis + 1
        else:
            higher = dis
    if discheck(positions, dis, balls):
        return lower
    else:
        return lower - 1

print(BallsForce(pos, Ba))