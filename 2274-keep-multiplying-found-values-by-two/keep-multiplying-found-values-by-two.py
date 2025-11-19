class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        nums.sort()
        for r in range(len(nums)):
            if ans == nums[r]:
                ans *= 2
        return ans