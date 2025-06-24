# '''lenght of window-count of most freq char<=k??
# then update res to max

# lenght of window=r-l+1

# '''
# s = "AABABBA"
# k = 1

# res=0
# l=0
# r=0
# hashmap={}
# for i in range(len(s)):
#     hashmap[s[i]]=1+hashmap.get(s[i],0)

#     while((r-l+1)-max(hashmap.values())>k):
#         hashmap[s[l]]-=1
#         l==1


#     res=max(res,r-l+1)

# return(res)


"""
:type s: str
:type k: int
:rtype: int
"""
s="BAAA"
k=0
i=0
maxlen=0
freqs = {}
for j in range(len(s)):
    print("hi")
    freqs[s[j]]=1+freqs.get(s[j],0)
    maxFreq = max(freqs.values())
    curlen=j-i+1
    while(curlen-maxFreq>k):
        print("inloop")
        freqs[s[i]]-=1
        i+=1
        curlen=j-i+1
        print(curlen, maxFreq,k)
    maxlen=max(maxlen,j-i+1)
    
print(maxlen)
print(freqs)
    

        