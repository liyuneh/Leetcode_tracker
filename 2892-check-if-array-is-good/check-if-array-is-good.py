class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        count = 0
        for x in nums:
            if x == mx:
                count += 1
        if count != 2:
            return False
        nums.sort()
        ans = [i + 1 for i in range(mx )]
        for i in range(len(nums) - 1):
            if ans[i] != nums[i]:
                return False
        return True