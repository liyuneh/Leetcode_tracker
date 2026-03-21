class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        for i in range(len(nums)):
            if i < len(nums) // 2 : count += max(0, nums[i] - k)
            elif i == len(nums) // 2 : count += (abs(nums[i] - k))
            else: count += max(0, k - nums[i])

        return count