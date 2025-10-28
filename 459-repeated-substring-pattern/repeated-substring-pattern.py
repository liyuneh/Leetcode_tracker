class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = 0
        for r in range(1,len(s)):
            if s[l] == s[r]:
                k = s[l:r]
                z = len(s) // (r - l )
                if s == (z * k):
                    return True
        return False