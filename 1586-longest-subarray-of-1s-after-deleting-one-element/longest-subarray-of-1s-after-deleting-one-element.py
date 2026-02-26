class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = []
        count = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
                l = i
        if l < len(nums):
            ans.append(count)
        print(ans)
        if len(ans) == 1:
            return max(0 , ans[0] - 1)
        want = 0
        for i in range(len(ans) - 1):
            x = ans[i] + ans[i+1]
            want = max(x, want)
        print(want)
        
        return want