class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = []
        l, r = 0, 1
        while r < len(nums):
            x = str(nums[l]) + str(nums[r])
            ans.append(int(x))
            l , r = l + 2, r + 2
        print(ans)
        ans.sort()
        return ans[0]