# l=["hi","hello",'little']
# print(enumerate(l)) makes [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hashmap of val->index

        hashmap={}
        for index,number in enumerate(nums):# ennumerate time comp is O(1)
            hashmap[number]=index
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashmap:
                return [index,hashmap[diff]]
