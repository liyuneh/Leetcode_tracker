class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for r in range(1,len(nums)):
            if nums[r] != nums[l]:
                l += 1
            else:
                return nums[l]