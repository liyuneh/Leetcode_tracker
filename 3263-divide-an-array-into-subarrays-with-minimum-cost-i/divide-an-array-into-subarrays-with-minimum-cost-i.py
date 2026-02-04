class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        arr = sorted(nums)
        if arr == nums:
            return sum(nums[:3])
        x1 = nums[0]
        arr1 = sorted(nums[1:])
        return x1 + sum(arr1[:2]) 
        