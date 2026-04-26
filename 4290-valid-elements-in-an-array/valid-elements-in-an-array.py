class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        front, back = [nums[0]],[nums[-1]]
        # print(front, back)
        if len(nums) == 1:
            return nums
        mx = max(nums)
        left, right = float('-inf'), [0] * len(nums)
        m = float("-inf")
        ans = []
        for i  in range(len(nums)- 1, - 1, -1):
            right[i] = m
            m = max(m, nums[i])
        for i in range(len(nums)):
            if i == 0 or i == len(nums) -1:
                ans.append(nums[i])
            elif nums[i] > left:
                ans.append(nums[i])
            elif nums[i] > right[i]:
                ans.append(nums[i])
            left = max(left, nums[i])
        return ans