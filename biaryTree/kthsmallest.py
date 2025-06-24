# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        res=0
        def dfs(node):
            nonlocal k
            nonlocal count
            nonlocal res
            if not node:
                return 0
            dfs(node.left)
            # print(node.val)
            count+=1

            if count==k:
                print(node.val)
                res=node.val
            dfs(node.right)
        dfs(root)
        return(res)
