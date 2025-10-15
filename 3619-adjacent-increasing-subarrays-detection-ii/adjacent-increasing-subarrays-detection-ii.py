class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        current , prev = 1, 0
        ans = 0
        for r in range(n - 1):
            if nums[r] < nums[r + 1]:
                current += 1
            else:
                prev = current
                current = 1
            ans = max(ans, current // 2, prev//2, min(prev, current))
        return ans