class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        pref = []
        
        l = 0
        while l < len(nums):
            r = l
            pref_sum = 0
            for r in range(r, len(nums)):
                pref_sum += nums[r]
                pref.append(pref_sum)
            l += 1
        pref.sort()
        return sum(pref[left - 1: right]) % (10 ** 9 + 7)