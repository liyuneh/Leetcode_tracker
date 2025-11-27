class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = [float('inf')] * k
        pref[0] = 0
        res = float('-inf')
        total = 0

        for i, n in enumerate(nums):
            total += n
            length = i + 1
            pref_len = length % k
            res = max(res, total - pref[pref_len])
            pref[pref_len] = min(total, pref[pref_len])
        return res
