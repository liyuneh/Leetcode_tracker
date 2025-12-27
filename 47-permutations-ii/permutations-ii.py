from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        p = permutations(nums)
        ans = []
        seen = set()
        for prem in p:
            t = tuple(prem)
            if t not in seen:
                seen.add(t)
                ans.append(t)
        return ans