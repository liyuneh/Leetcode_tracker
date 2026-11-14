class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        real = float('inf')
        for i in range(len(nums)):
            ans = 0
            for j in range(i, len(nums)):
                ans += nums[j]
                if l <= j - i + 1 <= r and ans > 0:
                    real = min(real, ans)
        print(real)
        return - 1 if real == inf else real