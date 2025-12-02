class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        ans = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                ans.append(nums[i])


        count = 1
        res = 1
        for i in range(1,len(ans)):
            if ans[i] == (ans[i-1] + 1):
                count += 1
            else:
                res = max(res , count)
                count = 1
            res = max(res, count)
        return res