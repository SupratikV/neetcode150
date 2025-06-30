class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[]
        count=0
        for i in range(len(s)):

            #odd palindrome
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res.append(s[l:r+1])
                count+=1
                l-=1
                r+=1
            
            #even palindrome
            l=i
            r=i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                res.append(s[l:r+1])
                count+=1
                l-=1
                r+=1

        return len(res)

        