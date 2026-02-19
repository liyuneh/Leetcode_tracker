class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mn = 0
        l , r = 0 , len(piles) - 2
        while l < r:
            mn += piles[r]
            l += 1
            r -= 2
        return mn