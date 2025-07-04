# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        res=0
        
        #calculates height
        def height(node):
            if not node:
                return 0
            left=height(node.left)
            right=height(node.right)
            nonlocal res
            res=max(res,left+right)
            return 1+max(left,right)
        
        height(root)
        return res
        
        
            
        