class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in seen:
                return nums1[i]
        return -1