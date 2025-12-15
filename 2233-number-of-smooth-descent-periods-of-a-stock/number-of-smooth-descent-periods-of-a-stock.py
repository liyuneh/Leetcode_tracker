class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = len(prices)
        l = 0
        for r in range(1, len(prices)):
            if prices[r] == prices[r- 1] - 1:
                count += (r - l )
            elif prices[r] + 1 != prices[r-1]:
                l = r
        return count