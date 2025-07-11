# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            if not node:
                return 0
            if node.val>=maxval:
                res=1
                maxval=node.val
            else:
                res=0
            res+=dfs(node.left,maxval)
            res+=dfs(node.right,maxval)
            return(res)
                
        return dfs(root,-100)
