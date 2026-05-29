class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = sum(int(digit) for digit in str(nums[i]))
        # print(min(nums))
        return min(nums)