class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        profit=0
        while r<len(prices):

            if prices[l]<prices[r]:
                pr=prices[r]-prices[l]
                if pr>profit:
                    profit=pr
            else:
                l=r
            r+=1
        return profit
            

        