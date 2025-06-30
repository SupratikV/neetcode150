# start from middle and move both sides
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        res=''

        for i in range(len(s)):
            #odd
            l,r=i,i

            while l>=0 and r<length and s[l]==s[r]:
                if (r-l+1)>len(res):
                    res=s[l:r+1]

                l-=1
                r+=1
            #even
            l,r=i,i+1
            while l>=0 and r<length and s[l]==s[r]:
                if (r-l+1)>len(res):
                    res=s[l:r+1]

                l-=1
                r+=1
        return res


