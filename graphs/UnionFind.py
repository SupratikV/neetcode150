#number of connected problems in an undirected gra
#count compoinents:
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank=[1]*n 
    
        def find(n):#finds the root parent
            while (n!=par[n]):
                par[n]=par[par[n]]
                n=par[n]
            return n


        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p1]+=rank[p1]
            return 1
        
        res=n
        for n1,n2 in edges:
            res-=union(n1,n2)
        return res
