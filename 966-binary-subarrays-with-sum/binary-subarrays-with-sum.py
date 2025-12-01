class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = {0:1}

        prefs = 0
        count = 0

        for ch in nums:
            prefs += ch

            if prefs - goal in pref:
                count += pref[prefs - goal]
            pref[prefs] = pref.get(prefs, 0) + 1
        return count