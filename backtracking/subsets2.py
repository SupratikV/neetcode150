# to prevent duplicates:
# 1. Sort the array
# 2. have while loop to skip same elements

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            # Include nums[i]
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            # Skip duplicates for the exclude path
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res
