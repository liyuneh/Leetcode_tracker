class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        ans = 0
        for i in range(len(gain)):
            ans += gain[i]
            mx = max(mx, ans)
        return mx