class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        res = 0
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res  = res * 10 + int(s[i])
            i += 1

            if res* sign > 2 ** 31 - 1 :
                return 2 ** 31 - 1
            elif res * sign < -2 ** 31 :
                return -2 ** 31 
        return res * sign

        
        return 