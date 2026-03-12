class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        ind = nums.index(0)
        print(ind)
        l = ind
        count = 0
        for r in range(ind,len(nums)):
            if nums[r] !=  nums[l]:
                count += 1
                l = r
        if nums[l] == nums[r]:
            count += 1
        return count   