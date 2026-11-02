class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = float("inf")
        l, r = 0, 1
        while r < len(nums):
            x = int(str(nums[l]) + str(nums[r]))
            ans = min(ans, x)
            l , r = l + 2, r + 2
        return ans