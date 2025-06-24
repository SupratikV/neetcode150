#return self.isBalanced(root.left) and self.isBalanced(root.right)
# NOTE: THE TREE IS BALANCED IF THE LEFT AND RIGHT SUBTREES ARE BALANCED

#BRUTE FORCE 0(N2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res=0
        
        #calculates height
        def height(node):
            if not node:
                return 0
            return(1+max(height(node.left),height(node.right)))
        
        #outer
        if not root:
            return True
        left=height(root.left)
        right=height(root.right)

        if abs(left-right)>=2:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
