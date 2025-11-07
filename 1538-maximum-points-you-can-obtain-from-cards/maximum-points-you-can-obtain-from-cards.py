class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if k == len(nums):
            return total
        lsum , rsum , max_s = 0 , 0 ,0
        for i in range(k):
            lsum += nums[i]
        max_s = lsum
        r = len(nums) - 1
        for i in range(k - 1 , - 1, -1):
            lsum -= nums[i]
            rsum += nums[r]
            r -= 1
            max_s = max(max_s, lsum + rsum)
        return max_s
