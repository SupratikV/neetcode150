class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]

        def dfs(i):
            print("hi", subset)
            if sum(subset)>target or i>=len(nums):
                return 0
            if sum(subset)==target:
                res.append(subset.copy())
                print(subset)
                return
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res6

# Backtracking is all about:

# Choose: Pick a letter for the current digit.
# Explore: Recurse to the next digit.
# Un-choose (Backtrack): Undo your choice to try other options.

            

# for all such quesitons draw diagram ull know.