class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque()
        freq = {}
        
        for i , ch in enumerate(s):
            freq [ch] = freq.get(ch, 0) + 1
            q.append((ch, i))

            while q and freq[q[0][0]] > 1:
                q.popleft()
        return q[0][1] if q else -1