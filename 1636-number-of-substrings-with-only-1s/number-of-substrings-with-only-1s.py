class Solution:
    def numSub(self, s: str) -> int:
        l = 0 
        count = 0
        mode = 10 **9 + 7
        for r in range(len(s)):
            if s[r] == '0':
                l = r + 1
            else:
                count += (r - l + 1)
        return count % mode