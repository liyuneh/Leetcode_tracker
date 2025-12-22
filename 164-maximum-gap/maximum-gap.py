class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap = abs(nums[1] - nums[0]) if len(nums) >= 2 else 0
        for i in range(2, len(nums)):
            if abs(nums[i] - nums[i-1]) > gap:
                gap = abs(nums[i] - nums[i-1])
        return gap