class Solution:
    def climbStairs(self, n: int, cost: List[int]) -> int:
        
        @lru_cache
        def dp(i):

            if i >= n:
                return 0
            
            best = float('inf')
            for d in range(1, 4):
                if i + d <= n:
                    best = min(best, dp(i + d) + cost[i + d  - 1] + d*d )
            return best
        return dp(0)