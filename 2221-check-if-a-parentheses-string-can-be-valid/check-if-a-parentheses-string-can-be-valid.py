class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        op , cl = 0 , 0
        l , r = 0 , len(s) - 1
        while l < len(s) - 1 and r >= 0:
            op += 1 if (s[l] == "(" or locked[l] == "0") else -1
            cl += 1 if (s[r] == ")" or locked[r] == "0") else -1
            # print(op, cl)
            if op < 0 or  cl < 0:
                return False
            l , r = l + 1, r - 1
        return True