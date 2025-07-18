# BFS is great for level order stuff,
#  like shortest path, finding all nodes at distance k, etc.
# But LCA is all about ancestry — who is above whom — so recursive DFS fits naturally.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.val==p.val or root.val==q.val:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        
        if left:
            return left

        return right 



        