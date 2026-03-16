class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        cur = 0
        i = 0
        num = 1
        while num <= n:
            while i < len(nums) and nums[i] <= num:
                cur += nums[i]
                i += 1
            if num > cur:
                ans += 1
                cur += num
            num = cur + 1
            
        return ans