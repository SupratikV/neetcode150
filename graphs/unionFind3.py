#redundant connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]*(n+1) 
    
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
            if not union(n1,n2):
                return [n1,n2]
        #received res now

