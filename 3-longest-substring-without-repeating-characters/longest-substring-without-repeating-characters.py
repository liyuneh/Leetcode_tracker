class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        count = 0
        for r in range(len(s)):
            while s[r] in q:
                q.popleft()
            q.append(s[r])
            count = max(count, len(q))
        return count