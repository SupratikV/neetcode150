from collections import deque
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = None
        self.right = None

#types are:
# recursive dfs: uses recursion
# iterative dfs: uses stack
# bfs: uses queue

#recusive dfs

def dfs(node):
    if not node:
        return None
    return(1+max(dfs(node.left),dfs(node.right)))

#interative  bfs

def bfs(node):
    q=deque([node])
    while q:
        for i in range(len(q)):
            ele=q.popleft()
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
        level+=1
    return level
    
#iterative dfs
def iterdfs(node):
    result=0
    stack=[[node,1]]
    while stack:
        node,depth=stack.pop()

        if node:
            res=max(res,depth)
            stack.append([node.left,depth+1])
            stack.append([node.right,depth+1])
    return res
           
