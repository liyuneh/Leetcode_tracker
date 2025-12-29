class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , ans = 0,float('inf')
        sum = 0
        r = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target and l <= r:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return ans if ans  != float('inf') else 0