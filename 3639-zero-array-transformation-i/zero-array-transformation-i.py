class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ans = [0] * len(nums)

        for left, right in queries:
            ans[left] += 1
            if right + 1 < n:
                ans[right + 1] -= 1
        dec = 0
        for i in range(n):
            dec += ans[i]
            if nums[i] > dec:
                return False
        return True