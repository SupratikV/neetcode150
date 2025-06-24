class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr=[]
        res=[]
        def dfs(i):
            nonlocal curr
            nonlocal res
            if i>=len(s):
                res.append(curr.copy())
                return 
            for j in range(i,len(s)):
                if self.isPalin(s[i:j+1]):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return res


    def isPalin(self,s):
        if s==s[::-1]:
            return True
        return False

        