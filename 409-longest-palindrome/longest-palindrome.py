class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = defaultdict(int)
        for ch in s:
            table[ch] += 1
        count = 0
        odd = False
        for val in table.values():
            count += (val // 2) * 2
            if val % 2 == 1:
                odd = True
        


        return count + 1 if odd else count