class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = {0:1}
        pref_sum = 0
        count = 0
        for ch in nums:
            pref_sum += ch

            if pref_sum - k in pref:
                count += pref[pref_sum - k]
            pref[pref_sum] =  pref.get(pref_sum, 0) + 1
        return count