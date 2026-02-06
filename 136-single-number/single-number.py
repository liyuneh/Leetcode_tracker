class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen= sum(set(nums))
        seen1 = sum(nums)
        return 2*seen - seen1
            