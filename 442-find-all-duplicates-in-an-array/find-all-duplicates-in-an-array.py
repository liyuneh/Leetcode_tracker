class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            if nums[x] > 0:
                nums[x] = - nums[x]
            else:
                ans.append(abs(nums[i]))
        return ans     