class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        mx = False
        for i in range(1,min(10 ** 5, max(max(nums) + 1, 2))):
            if i not in seen:
                mx = True
                return i
        if not mx:
            return max(nums) + 1