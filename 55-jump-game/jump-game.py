class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = nums[0]
        if count == 0 and len(nums) != 1:
            return False
        if count == 0 and len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if count - 1 < nums[i]:
                count = nums[i]
            else:
                count -= 1
            if count  == 0 and i != len(nums) - 1:
                return False
        return True
            