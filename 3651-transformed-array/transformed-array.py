class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        arr = nums[::-1]
        for i in range(len(nums)):
            if nums[i] > 0 :
                ans.append(nums[(nums[i] + i ) % n])
            elif nums[i] < 0 :
                ans.append(arr[(abs(nums[i]) + (n - (i + 1)))% n])
            else:
                ans.append(nums[i])
        return ans