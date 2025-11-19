class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l , r = 0 , 0
        n , m = len(nums1), len(nums2)
        ans = []
        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                ans.append(nums1[l])
                l += 1
            else:
                ans.append(nums2[r])
                r += 1
        if l < n:
            ans += nums1[l:]
        else:
            ans += nums2[r:]
        length = len(ans)
        mid = length // 2

        if length % 2 == 1:
            return float(ans[mid])
        else:
            return (ans[mid - 1] + ans[mid]) / 2