class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        par=[i for i in range(n)]
        rank=[1]*n
        def find(n):
            while par[n]!=n:
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
                rank[p2]+=rank[p1]
            return 1
        
        res=n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    res-=union(i,j)
        return res




        
        