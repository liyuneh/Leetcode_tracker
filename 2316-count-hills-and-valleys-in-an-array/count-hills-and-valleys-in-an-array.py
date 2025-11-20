class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l = count = 0
        ans = []
        for num in nums:
            if not ans or ans[-1] != num:
                ans.append(num)
        r = 1
        while  r < len(ans) - 1:
            if ans[r] > ans[l] and ans[r] > ans[r+ 1]:
                count += 1
            elif ans[r] < ans[l] and ans[r] < ans[r + 1]:
                count += 1
            l += 1
            r += 1
        return count