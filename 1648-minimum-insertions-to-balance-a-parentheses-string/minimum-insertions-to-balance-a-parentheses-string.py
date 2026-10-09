class Solution:
    def minInsertions(self, s: str) -> int:
        res , open , i = 0 , 0 , 0
        while i < len(s):
            if s[i] == "(":
                open += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 2
                else:
                    res += 1
                    i += 1
                if open :
                    open -= 1
                else:
                    res += 1
        res += 2 * open
        print(res)
        return res