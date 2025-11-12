class Solution:
    def isValid(self, s: str) -> bool:
        br = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c not in br:
                stack.append(c)
            elif stack and stack[-1] == br[c]:
                stack.pop()
            else:
                return False
        return not stack