class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            l , r = s.index(letter) , s.rindex(letter)
            between = set()

            for k in range(l + 1, r):
                between.add(s[k])
            ans += len(between)
        return ans