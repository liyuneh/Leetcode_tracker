class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        k = 0
        for x in nums:
            if x >= 0:
                seen.append(x)
                k = 0
            else:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[-k])
        return ans
