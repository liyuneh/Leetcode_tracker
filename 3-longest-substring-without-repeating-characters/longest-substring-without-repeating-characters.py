class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in q:
                q.remove(s[l])
                l += 1
            q.add(s[r])
            count = max(count, r - l + 1)
        return count