"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen={}

        def dfs(node):
            if not node:
                return

            if node in seen:
                return seen[node]

            copy=Node(node.val)
            seen[node]=copy

            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            
            return copy

        return dfs(node)


        