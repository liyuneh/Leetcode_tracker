class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        new = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == new:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count += 1
                    new = nums[i]
        return new