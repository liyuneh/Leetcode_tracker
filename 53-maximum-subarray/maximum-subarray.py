class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        Sum = 0
        for i in range(len(nums)):
            Sum = max(nums[i], Sum + nums[i])
            best = max(best , Sum)
        return best
        