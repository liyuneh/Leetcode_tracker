class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) - 1
        mn = float("inf")
        # while left <=  right:
        #     mid = left + (right - left) // 2
        #     if nums[left] >= nums[right]:
        #         mn = min(mn, nums[left])
        #         left = mid + 1
        #     elif nums[left] < nums[right]:
        #         mn = min(mn, nums[right])
        #         right = mid - 1
        #     print(nums[left], nums[right])
        return min(nums)

