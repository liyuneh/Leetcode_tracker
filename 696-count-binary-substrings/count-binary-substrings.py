class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                l , r = i , i + 1
                while l >= 0 and r < len(s) :
                    if s[l] == s[i] and s[r]== s[i+1]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
        return count
