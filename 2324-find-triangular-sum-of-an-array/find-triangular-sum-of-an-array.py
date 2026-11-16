class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:

            ans = []
            for i in range(len(nums) - 1):
                ans.append((nums[i] + nums[i +1]) % 10)
            n -= 1
            nums[:] = ans
        # print(nums[0])
        return nums[0]