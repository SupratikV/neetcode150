# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.


#for this question, we willl use dfs and pass left/right values every recursion

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validbst(node,left,right):
            if not node:
                return True
            if node.val<=left or node.val>=right:
                return False
            return(validbst(node.left,left,node.val) and validbst(node.right,node.val,right))


        return(validbst(root,-1000,1000))