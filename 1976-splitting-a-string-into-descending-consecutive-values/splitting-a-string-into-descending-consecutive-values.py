class Solution:
    def splitString(self, s: str) -> bool:
        res = []
        def backtrack(start):
            if start >=  len(s):
                return len(res) >= 2
            for i in range(start, len(s)):
                valid = int(s[start:i + 1])
                if len(res) == 0 or valid == res[-1] - 1:
                    res.append(valid)
                    if backtrack(i + 1):
                        return True
                    res.pop()
            return False
        return backtrack(0)