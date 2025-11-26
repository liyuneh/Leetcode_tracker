class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        k = 0
        for c , p in enumerate(s):
            if p == '(':
                k += 1
            elif  p == ')':
                k -= 1
                if c > 0 and s[c-1] == "(":
                    count += 2 ** k

        return int(count)