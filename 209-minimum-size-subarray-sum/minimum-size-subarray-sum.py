class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l , Sum = 0 ,0
        count = float('inf')
        for r in range(len(nums)):
            Sum += nums[r]
            while Sum >= target:
                count = min(count, r - l + 1)
                Sum -= nums[l]
                l += 1
        return count  