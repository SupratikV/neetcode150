# in a tree:
# 1) no cycles
# 2) all nodes are connected

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit=set()
        adjlist={i:[] for i in range(n)}

        for node,edge in edges:
            adjlist[node].append(edge)
            adjlist[edge].append(node)
        #adjlist is ready now

        def dfs(cur,prev):
            if cur in visit:
                return False #cuz cycle is found
        
            visit.add(cur)
            for i in adjlist[cur]:
                if i==prev:
                    continue
                if not dfs(i,cur):
                    return False
            return True
        print(adjlist)
        print(visit)
        return(dfs(0,-1) and len(visit)==n)
            
            

            