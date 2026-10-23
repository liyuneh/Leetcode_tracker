class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, len(nums)):
            found = False
            for j in range(i - 1, -1, -1):
                if -target <= nums[i] - nums[j] <= target:
                    dp[i] = max(dp[i], dp[j] + 1 if dp[j] > 0 else 0)
                    found = True
            if not found:
                dp[i] = 0
        print(dp)
        return dp[n-1] - 1