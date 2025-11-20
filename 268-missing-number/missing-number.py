class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = max(nums)
        seen = set(nums)
        for i in range(0, s + 2):
            if i not in seen:
                return i