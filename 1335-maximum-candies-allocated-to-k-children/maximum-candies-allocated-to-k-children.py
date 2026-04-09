class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can(candies, k, portion):
            count = 0
            for i in range(len(candies)):
                count += (candies[i] // portion)
            return count >= k
        l , r = 1, max(candies)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if can (candies, k, mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans