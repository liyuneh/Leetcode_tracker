class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        ans = []
        for c in nums:
            seen[c] = seen.get(c, 0) + 1
            if seen[c] <= 2:
                ans.append(c)
        nums[:] = ans
        return len(nums)