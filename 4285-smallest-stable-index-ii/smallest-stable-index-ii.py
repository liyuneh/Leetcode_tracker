class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx = nums[0]
        mx1 = [mx:=max(mx, x) for x in nums]
        mn = nums[-1]
        mn1 = [mn := min(mn, x) for x in reversed(nums)]
        mn1.reverse()
        for i in range(len(mx1)):
            if mx1[i] - mn1[i] <= k:
                return i
        return -1