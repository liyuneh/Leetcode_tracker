class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = defaultdict(int)
        for ch in s:
            table [ch] += 1
        for i in range(len(s)):
            if table[s[i]] == 1:
                return i
        return -1
        