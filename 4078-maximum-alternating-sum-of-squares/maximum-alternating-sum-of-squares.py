class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [-x if x < 0 else x for x in nums]
        nums.sort()
        total = 0
        l , r = 0 , len(nums) - 1
        # print(nums)
        while l < r :
            total += ((nums[r]) ** 2 - (nums[l] ** 2))
            l += 1
            r -= 1
        if len(nums) % 2 != 0 :
            total += (nums[len(nums) // 2] ** 2)
        # print(total)
        return total 