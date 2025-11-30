class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , ans = 0 , float('inf')
        Sum = 0
        r = 0
        while r < len(nums):
            Sum += nums[r]
            while Sum >= target:
                ans = min(ans,r - l + 1)
                Sum -= nums[l]
                l += 1
            r += 1
        return ans if ans != float('inf') else 0
