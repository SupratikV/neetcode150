#to find maximum window sum

def fixed_window(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(window_sum,max_sum)
    
    return max_sum