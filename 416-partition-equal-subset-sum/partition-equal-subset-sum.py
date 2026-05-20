class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n)]

        def memo(idx, rem):
            if rem == 0:
                return True
            if rem < 0 or idx >= len(nums):
                return False
            if dp[idx][ rem] != -1:
                return dp[idx][rem]
            include  = memo(idx + 1,  rem - nums[idx])
            exclude = memo(idx + 1, rem)
            dp[idx][rem] = include or exclude
            return dp[idx][rem]
        return memo(0,  total // 2)
                