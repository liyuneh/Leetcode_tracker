class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def left():
        #     l, r = 0 , len(nums) - 1
        #     while l <= r:
        #         mid = l + (r - l ) // 2
        #         if nums[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return l
        # def right():
        #     l , r = 0 , len(nums) - 1
        #     while l <= r:
        #         mid = l + (r - l ) // 2
        #         if nums[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return r
        # left , right = left(), right()
        # if left <= right and nums[left] == nums[right]:
        #     return [left, right]
        # else:
        #     return [-1,-1]
        if not nums:
            return [-1,-1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        right = right - 1 if right != 0  else 0
        if left <= right and nums[left] == nums[right] == target: 
            return [left, right]
        else:
            return [-1,-1]