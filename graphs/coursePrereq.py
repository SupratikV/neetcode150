# here we check if graph has cycle
# as if cycle, then false

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        visit=set()

        for crs,pre in prerequisites:
            premap[crs].append(pre)
        
        #premap is now ready. maps each course to its prerequisites

        def dfs(crs):
            if crs in visit:
                return False
            
            if premap[crs]==[]:
                return True
            
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            premap[crs]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




        