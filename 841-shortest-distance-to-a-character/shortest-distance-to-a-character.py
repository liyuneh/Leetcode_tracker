class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0] * len(s)
        dist = float('inf')
        for i in range(len(s) - 1, - 1, -1):
            if s[i] == c:
                dist = 0
            else:
                dist += 1
            ans[i] = dist
        dist = float('inf')
        for i in range(len(s)):
            if s[i] == c:
                dist = 0
            else:
                dist += 1
            ans[i] = min(ans[i], dist)
        return ans