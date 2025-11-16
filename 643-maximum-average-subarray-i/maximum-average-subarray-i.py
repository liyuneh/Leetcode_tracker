class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        Sum = 0
        max_count = float(-inf)
        for r in range(len(nums)):
            Sum += nums[r]
            if r - l + 1 == k:
                max_count = max(max_count, Sum / k)
                Sum -= nums[l]
                l += 1
        return max_count