'''time complexity for searching in set: O(1)'''

# hashmap={}
# s = "zxyzxyz"
# charSet=set()
# l=0
# res=0

# for r in s:
#     while s[r] in charSet:
#         charSet.remove(s[l])
#         l+=1
#     charSet.add(s[r])
#     res = max(res, r - l + 1)
# print(res)


"""
:type s: str
:rtype: int
"""
s="abcabcbb"
i=0
max_length=0
setm=set()
for j in range(0,len(s)):
    j+=1 
    while(s[j] in setm):
        i+=1
    setm.add(s[j])

    if j-i+1>max_length:
        max_length=j-i+1
        print(max_length)
    print("j is :",j)
print(max_length)
