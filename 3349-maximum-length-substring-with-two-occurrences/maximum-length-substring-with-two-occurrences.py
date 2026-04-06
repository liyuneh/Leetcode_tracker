class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l , tot = 0 , 0
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            while freq[s[i]] > 2:
                freq[s[l]] -= 1
                l += 1
            tot = max(tot, i - l + 1)
        print(tot)
        return tot