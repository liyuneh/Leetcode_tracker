class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , ans = 0,  0
        count = float('inf')
        for right in range(len(nums)):
            ans += nums[right]
            while ans >= target:
                count = min(count, right-left + 1)
                ans -= nums[left]
                left += 1
        return 0 if count == float('inf') else count
