class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        mn = nums[-1]
        for i in range(len(nums) - 2, - 1, -1):
            if nums[i] > mn:
                c = math.ceil(nums[i] / mn)
                count += (c - 1)
                mn = nums[i] // c
            else:
                mn = nums[i]
            
        return count 