class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return min(cost1 * need1 + cost2 * need2 , costBoth * max(need1, need2) , costBoth * min(need1 , need2) + cost1 * (need1 - min(need1, need2)) + cost2 * (need2 - min(need1, need2)))