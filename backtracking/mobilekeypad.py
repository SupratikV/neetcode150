class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        curr=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def dfs(i):
            if i==len(digits):
                res.append(''.join(curr.copy()))
                return
            for c in digitToChar[digits[i]]:
                curr.append(c)
                dfs(i+1)
                curr.pop()
        if digits:
            dfs(0)

        return res
            
            
        