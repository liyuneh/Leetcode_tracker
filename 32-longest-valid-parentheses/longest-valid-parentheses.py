class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_len = i - stack[-1]
                    if current_len > count:
                        count = current_len
        return count