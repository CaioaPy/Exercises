#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key
#plus the sum of all keys greater than the original key in BST.

#As a reminder, a binary search tree is a tree that satisfies these constraints:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

#e. g.
#Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

#binary search tree = 
#                 ----4----
#              1/           \6
#          0/    \2      5/    \7
#                 \3            \8

import math

Bst = [4,1,6,0,2,5,7,0,0,0,3,0,0,0,8]

def BstToGst(BstRoot):
    Gst = []
    for i in BstRoot:
        Gst.append(0)
    levels_holder = (len(BstRoot) - 1)
    total_levels = 0
    while levels_holder != 0:
        levels_holder = levels_holder // 2
        total_levels += 1
    levels = total_levels 
    
    level_slot = 1
    for n in range (1, levels + 2):
        global max
        aux = n
        n = BstRoot[-(n)]
        if n != 0:
            i = ((aux + levels) + (level_slot * 2) - (level_slot))
            n += BstRoot[-i]
            Gst[-aux] = n
            level_slot += 1
            max = aux
    
    loop_levels = levels / 2
    loop_levels = math.ceil(loop_levels)
    levels = levels * 2
    level_slot = 0
    for n in range (1, levels + 3):
        aux = n
        n = BstRoot[-(n)]
        if n != 0:
            print(f"loop_levels {loop_levels}")
            print(f"aux {aux}")
            if n in Gst:
                print("a")
            else:
                i = ((aux + loop_levels) + (level_slot * 2) - (level_slot))
                print(f"i {i}")
                print(f"n {n}")
                n += BstRoot[-i]
                print(f"n2 {n}")
                Gst[-aux] = n
            level_slot += 1
            max = aux

    print(Gst)

BstToGst(Bst)