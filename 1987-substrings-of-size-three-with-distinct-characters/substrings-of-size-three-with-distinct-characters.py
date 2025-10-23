class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        for r in range(len(s)):
            if r - l + 1 == 3 :
                if  s[l] != s[r - 1 ] and s[r - 1] != s[r] and s[l] != s[r]:
                    count += 1
                l += 1
                
        return count
