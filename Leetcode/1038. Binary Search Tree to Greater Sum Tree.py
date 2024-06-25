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

Bst = [4,1,6,0,2,5,7,0,0,0,3,0,0,0,8]

def BstToGst(BstRoot):
    Gst = []
    levels_holder = (len(BstRoot) - 1)
    total_levels = 0
    while levels_holder != 0:
        levels_holder = levels_holder // 2
        total_levels += 1
    levels = total_levels 
    
    x = 1
    for n in range (x, levels + 2):
        n = BstRoot[-(n)]
        if n != 0: 
            n += BstRoot[-((n + levels) + (levels - 1))]
            print(n)

    

BstToGst(Bst)