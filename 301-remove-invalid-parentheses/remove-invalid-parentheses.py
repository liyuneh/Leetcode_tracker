class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        mx = 0
        res = set()
        def backtrack(i, path):
            if i == len(s):
                if isValid(path):
                    nonlocal mx, res
                    if len(path) > mx:
                        res = set()
                        mx = len(path)
                    if len(path) == mx:
                        res.add(path)

                return 
            if s[i] in "()":
                backtrack(i+1, path)
            backtrack(i+1, path + s[i])
        backtrack(0 , "")
        return list(res)