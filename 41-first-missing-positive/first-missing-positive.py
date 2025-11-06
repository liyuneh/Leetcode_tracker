class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n , m = len(nums) , max(nums)
        if 1 not in nums:
            return 1
        seen = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in seen:
                return i
        return len(nums) + 1