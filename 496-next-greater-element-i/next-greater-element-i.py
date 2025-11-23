class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for n in nums1:
            x = nums2.index(n)
            found = -1
            for i in range(x, len(nums2)):
                if nums2[i] > n:
                    found = nums2[i]
                    break
            stack.append(found)
        return stack
                