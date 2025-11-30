class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        res = 0
        for l in range(len(nums)):
            count = 1
            r = l
            right = False
            while r + 1 < len(nums) and nums[r + 1] > nums[r]:
                r += 1
                count += 1
            while r + 1 < len(nums) and r != l and nums[r + 1] < nums[r]:
                r += 1
                count  += 1
                right = True
            if l != r and right and count > 2:
                res = max(res, count)
                r -= 1
            l = r
        return res