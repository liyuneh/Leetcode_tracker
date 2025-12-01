class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) <= 1:
            return 0

        ans = float('inf')
        for r in range(len(nums)- k + 1):
            ans = min(ans, nums[r+k-1] - nums[r])
        return ans