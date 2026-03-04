class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ans = {0:-1}
        pref = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] == 0:
                return True
        for i , num in enumerate(nums):
            pref += num
            x = pref % k
            if x in ans:
                if i - ans[x] >= 2:
                    return True
            else:
                ans[x] = i
        return False