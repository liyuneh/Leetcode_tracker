class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        nums = nums[:k]
        # print(nums)

        i = ans =  0
        while mul > 0 and i < len(nums):
            ans += (nums[i] * mul)
            mul -= 1
            i += 1
        if i < len(nums):
            ans += sum(x for x in nums[i:])
        # print(ans, i)

        return ans