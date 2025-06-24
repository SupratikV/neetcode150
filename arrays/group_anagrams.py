from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]
hashmap=defaultdict(list)
for word in strs:
    array=[0]*26
    for letter in word:
        array[ord(letter)-97]+=1
    hashmap[tuple(array)].append(word)
return list(hashmap.values())
    
    
