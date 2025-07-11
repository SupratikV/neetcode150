# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.equals(root,subRoot):
            return True
        return (self.isSubtree(root.right,subRoot)or self.isSubtree(root.left,subRoot))
        
        
    def equals(self,root,subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val==subroot.val :
            return(self.equals(root.left,subroot.left)and self.equals(root.right,subroot.right))
        return False
        