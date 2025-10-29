class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                old = stack.pop()
                prices[old] -= prices[i]
            stack.append(i)
        return prices