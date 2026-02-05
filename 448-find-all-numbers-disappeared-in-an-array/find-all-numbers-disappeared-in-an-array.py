class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            if nums[x] > 0:
                nums[x] = - nums[x]
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans