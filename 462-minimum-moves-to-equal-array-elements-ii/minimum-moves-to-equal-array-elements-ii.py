class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[len(nums) // 2]
        return sum(abs(x - i) for i in nums)