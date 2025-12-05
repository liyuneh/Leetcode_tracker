class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        count = 0
        for i in range(len(nums) - 1):
            prefix += nums[i]
            if (total - prefix) % 2 == prefix % 2:
                count += 1
        return count
