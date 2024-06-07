from typing import List

def numWays(words: List[str], target: str) -> int:
    ways = 0
    for c in target:
        targetC = list(target)
        i = 0
        j = 0
        word = []
        while i < 5 and j < 5:
            if (c == words[i][j]):
                word.append(words[i][j])
            elif (word == targetC):
                ways += 1
                word.pop(0)
                word.pop(0)
                word.pop(0)
            
    return ways
                
words = ["acca","bbbb","caca", "eeww", "fksa"]
target = "fae"
print(numWays(words, target))
