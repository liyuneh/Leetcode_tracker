class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        pref = num 
        i = len(num)
        while i > 0 and pref[i- 1] == '0':
            pref = pref[:-1]
            i -= 1
        return pref 