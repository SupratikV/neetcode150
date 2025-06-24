'''h>=len(array) as it can only eat one pile at a time.
k will be maximum the largest element of list. 
brute force-> intit speed to 1 and increment in each iteration till speed= largest element o(mxn)'''
import math
piles = [1,4,3,2]
h = 9
l=1
time=0
res=max(piles)
r=res
piles.sort()
speed=1
while l<=r:
    speed=(l+r)//2
    time=0
    for i in piles:
        time+=math.ceil(i/speed)
        # if time>h:
        #     break
    if time<=h:
        res=speed
        r=speed-1
    else:
        l=speed+1

print(res)