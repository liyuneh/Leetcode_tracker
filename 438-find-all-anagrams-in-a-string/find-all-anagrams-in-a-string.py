class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        ans = []
        need = Counter(p)
        window = Counter()
        for r in range(len(s)):
            window[s[r]] += 1

            if r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            if window == need :
                ans.append(l)
        return ans