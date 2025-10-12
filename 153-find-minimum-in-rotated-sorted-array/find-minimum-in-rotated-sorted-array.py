class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[middle + 1] :
                return nums[middle + 1]
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1