class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif stack and ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)