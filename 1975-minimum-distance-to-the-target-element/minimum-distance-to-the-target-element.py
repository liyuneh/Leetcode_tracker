class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mn = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                mn = min(mn, abs(i - start))
        print(mn)
        return mn