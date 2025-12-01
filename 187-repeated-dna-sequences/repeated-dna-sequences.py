class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seen = set()
        repeated = set()
        l = 0
        for r in range(len(s)):
            if r - l + 1 == 10:
                seq = s[l:r+1]
                if seq not in seen:
                    seen.add(seq)
                else:
                    repeated.add(seq)
                l += 1
        return list(repeated)
                