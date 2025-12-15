class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        n = len(nums)
        cnt = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
        return j