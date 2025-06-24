# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return([])
        q=deque([root])
        l=[[root.val]]
       

        while q:
            l.append([])
            for i in range(len(q)):
                ele=q.popleft()
                if ele.left:
                    q.append(ele.left)
                    l[-1].append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    l[-1].append(ele.right.val)
        l.pop()
        return l
