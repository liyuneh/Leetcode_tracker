class Solution:
    def check(self, nums: List[int]) -> bool:
        if sorted(nums) == nums:
            return True

        ans = []
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                ans.append(i)
        return len(ans) == 1 and nums[0] >= nums[-1]
        