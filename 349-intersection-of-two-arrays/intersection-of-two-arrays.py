class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1.sort()
        # nums2.sort()
        # l , r = 0 ,0 
        # ans = []
        # while l < len(nums1) and r < len(nums2):
        #     if nums1[l] == nums2[r]:
        #         if not ans or ans[-1] != nums1[l]:
        #             ans.append(nums1[l])
        #         l += 1
        #         r += 1
        #     elif  nums1[l] > nums2[r]:
        #         r += 1
        #     else:
        #         l += 1
        # return ans
        return list(set(nums1) & set(nums2))
            
            