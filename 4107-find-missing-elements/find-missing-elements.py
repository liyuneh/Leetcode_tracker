class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set(nums)
        for i in range(min(nums), max(nums) + 1):
            if i not in seen:
                ans.append(i)
        return ans
