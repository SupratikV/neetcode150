'''NOTE: DONT USE SLICING AS IT WILL MESS UP INDICES!!!'''
nums=[1,2,3,4,5,6,7,8,9,10]
target=5

l=0
r=len(nums)-1

while l<=r:
    mid=(l+r)//2

    if nums[mid]<target:
        l=mid+1
    elif nums[mid]>target:
        r=mid-1
    else:
        print(mid)
        break
print(-1)
