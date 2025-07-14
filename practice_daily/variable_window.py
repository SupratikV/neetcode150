def variable_window(arr,target):
    left=0
    window_sum=0
    min_length=float('inf')
    for right in range(len(arr)):
        window_sum+=arr[right]# expand window by usung right pointer
        if window_sum>target:
            min_size=min(min_size,right-left+1)#shrink window with left pointer
            window_sum-=arr[left]
            left+=1
    return min_length



