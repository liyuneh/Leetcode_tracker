class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = [0],[0]
        for i in range(1, len(nums)):
            left.append(left[-1] + nums[i - 1])

        for i in range(len(nums) - 2, -1 , -1):
            right.append(right[-1] + nums[i + 1])
        right.reverse()
        # print(left, right)
        for i in range(len(nums)):
            nums[i] = abs(left[i] - right[i])
        return nums