class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr.sort(key = lambda x:x[0])
        if arr[-1][0] >= arr[-2][0] * 2:
            return arr[-1][1]
        return -1