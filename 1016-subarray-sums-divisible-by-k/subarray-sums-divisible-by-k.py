class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curSum = 0
        pref = {0:1}
        res = 0

        for n in nums:
            curSum += n
            diff = curSum % k

            res += pref.get(diff, 0)
            pref[diff] =  pref.get(diff, 0) + 1
        return res