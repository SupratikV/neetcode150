class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

#Traversal:
'''types of traversal:
1.DFS: pre order(RooLR),inorder(LRooR),post order
2.BFS:
'''

def preOrderTraversal(node):
    if node==None:
        return
    print(node.data)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node==None:
        return
    preOrderTraversal(node.left)
    print(node.data)
    preOrderTraversal(node.right)
    
preOrderTraversal(root)
print("next")
inOrderTraversal(root)