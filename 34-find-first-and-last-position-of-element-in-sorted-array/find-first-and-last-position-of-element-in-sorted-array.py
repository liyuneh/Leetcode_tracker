class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        def right():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        left , right = left(), right()
        if left <= right and nums[left] == nums[right]:
            return [left, right]
        else:
            return [-1,-1]
            