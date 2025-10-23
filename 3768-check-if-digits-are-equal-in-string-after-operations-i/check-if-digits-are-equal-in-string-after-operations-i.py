class Solution:
    def hasSameDigits(self, s: str) -> bool:
        num = ""
        while len(s) > 2:
            for r in range(len(s) - 1):
                num += str((int(s[r] ) + int(s[r+1])) % 10)
            s = num
            num = ""
        if s[0] == s[1]:
            return True
        return False
