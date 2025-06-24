# nums=[4,5,6,7]
# [5,6,1,2,3,4]
nums=[3,4,5,6,1,2]
l=0
minimum=nums[0]
r=len(nums)
while l<r:
    middle=(l+r)//2
    print("middle:",middle)
    if nums[middle]<=minimum:
        minimum=nums[middle]
        r=middle
    else:
        l=middle+1
        print("l:",l,"r:",r)
print(minimum)