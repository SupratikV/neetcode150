# nums=[3,4,5,6,1,2]
# nums=[3,5,6,0,1,2]
nums=[3,4,5,6,1,2]
target=1
l=0
r=len(nums)-1
while l<=r:
    middle=(l+r)//2
    print("middle:",middle)
    if nums[middle]>target:
        l=middle+1
    elif nums[middle]<target:
        r=middle
        print("l:",l,"r:",r)
print(-1)