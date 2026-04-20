from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        ans = SortedList()
        count = 0
        for i in range(n):
            val = nums1[i] - nums2[i] 
            
            count += ans.bisect_right(val+ diff)
            ans.add(val)
        return count