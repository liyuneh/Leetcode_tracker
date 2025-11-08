class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        countin = 1
        countout = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        countout += 1
        return countout