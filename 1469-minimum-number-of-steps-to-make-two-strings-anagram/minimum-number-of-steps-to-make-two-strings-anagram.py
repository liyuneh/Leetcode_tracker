class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t = Counter(s) - Counter(t)
        sum1 = 0
        for val in t.values():
            sum1 += val
        return sum1