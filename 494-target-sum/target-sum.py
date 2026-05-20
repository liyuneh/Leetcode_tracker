class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(idx, total):
            if idx >= len(nums):
                if total  == target:
                    return True
                return False
            if  (idx, total) in memo:
                return memo[(idx, total)]
            exclude, include = dfs(idx + 1, total - nums[idx]),dfs(idx + 1, total + nums[idx ])
            memo[(idx , total )] = include + exclude
            return memo[(idx, total)]
        return dfs(0, 0)