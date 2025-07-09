# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(node,target):
            # nonlocal targetSum
            if not node:
                return False
            target+=node.val
            if target==targetSum:
                print('yea')
            if target==targetSum and not node.left and not node.right:
                return True
            
            print(target)
            
            return(dfs(node.left,target) or dfs(node.right,target))
            
        
        return(dfs(root,0))
