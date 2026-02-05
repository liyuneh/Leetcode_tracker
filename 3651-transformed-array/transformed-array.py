class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(nums[i] + i) % len(nums)] for i in range(len(nums))]