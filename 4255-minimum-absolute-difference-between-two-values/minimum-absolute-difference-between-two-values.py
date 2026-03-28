class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ans = []
        for i , n in enumerate(nums):
            if n == 1 or n == 2:
                ans.append((n,i))
        if len(ans) == 1:
            return -1
        mx = float("inf")
        for i in range(1,len(ans)):
            if ans[i][0] != ans[i-1][0]:
                mx = min(mx, abs(ans[i][1] - ans[i-1][1]))
        return mx if mx != float("inf") else -1