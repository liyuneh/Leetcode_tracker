class Solution:
    def romanToInt(self, s: str) -> int:
        D = {
            "I":1, "V":5 , "X": 10, "L":50 , "C":100, "D":500, "M":1000
        }
        ans , n= 0, len(s)
        i = 0
        while i < n:
            if i < n - 1 and D[s[i]] < D[s[i+1]]:
                ans += (D[s[i + 1]] - D[s[i]])
                i += 1
            else:
                ans += D[s[i]]
            i += 1
        return ans