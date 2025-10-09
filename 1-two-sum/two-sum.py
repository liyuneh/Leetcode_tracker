class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums and i != nums.index(result):
                return [i, nums.index(result)]