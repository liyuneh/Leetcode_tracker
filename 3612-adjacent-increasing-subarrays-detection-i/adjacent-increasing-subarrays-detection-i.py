class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ans = [0] * n
        cur = 0
        l = 0
        for r in range(n):
            if nums[r] <= nums[r - 1]:
                l = r
            if r - l + 1 == k:
                ans[l] = 1
                if l - k >= 0 and ans[l - k]:
                    return True
                l += 1
        print(ans)
        return False
            