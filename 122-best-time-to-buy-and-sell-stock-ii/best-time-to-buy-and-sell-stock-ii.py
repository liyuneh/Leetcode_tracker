class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , ans = 0, 0
        for r in range(1,len(prices)):
            if prices [r] > prices[r-1]:
                ans += (prices[r] - prices[r-1])
        return ans