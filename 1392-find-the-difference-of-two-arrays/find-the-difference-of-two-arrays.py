class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen = set(nums1)
        seen1 = set(nums2)

        return [list(seen - seen1), list(seen1-seen)]