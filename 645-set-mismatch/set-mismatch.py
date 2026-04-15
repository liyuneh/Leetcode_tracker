class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = -1
        for i in range(len(nums)):
            x = abs(nums[i])
            if nums[x- 1] > 0:
                nums[x - 1] = - nums[x-1]
            else:
                ans = x
        k = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                k = i + 1
                break

        return [ans, k]
