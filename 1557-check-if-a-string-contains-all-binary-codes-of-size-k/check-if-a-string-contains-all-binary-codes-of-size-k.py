class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        l  = 0
        for r in range(len(s)):
            if r - l + 1 == k :
                if s[l:r + 1] not in seen:
                    seen.add(s[l:r+1])
                l += 1

        return len(seen) == (2 ** k)