class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        #[rob1,rob2,n,n+1]
        for n in nums[1:]:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        rob1=0
        rob3=0
        for n in nums[:-1]:
            temp=max(n+rob1,rob3)
            rob1=rob3
            rob3=temp
        
    
        return(max(rob2,rob3))
