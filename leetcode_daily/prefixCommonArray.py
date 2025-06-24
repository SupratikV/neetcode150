A=[1,3,2,4]
B=[3,1,2,4]
res=[]
hashmap={}
sum=0
for i in range(len(A)):
    hashmap[A[i]]=1+hashmap.get(A[i],0)
    hashmap[B[i]]=1+hashmap.get(B[i],0)
    if B[i]!=A[i]:
        if hashmap[B[i]]==2:
            sum+=1
        if hashmap[A[i]]==2:
            sum+=1
        print("entered if! sum is:",sum)
    else:
        if hashmap[B[i]]==2:
            sum+=1    
    res.append(sum)
print(res)


        
        