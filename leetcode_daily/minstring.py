s = list("abaacbcbb")
hashmap={}
s1=""

for i in s:
    hashmap[i]=1+hashmap.get(i,0)
print(hashmap)
minus=0

indice=0
while indice<len(s):
    if hashmap[s[indice]]>=3:
        # letter=s[indice]
        # middle=indice+s[indice+1:].index(letter)+1
        # last=middle+s[middle+1:].index(letter)+1
        # del s[last]
        # print(middle)
        hashmap[s[indice]]-=2
        minus+=2
        indice+=1
        continue
    # s1+=s[indice]
    # indice+=1
    indice+=1


print(len(s)-minus)

# can also use from collections import Counter