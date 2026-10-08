class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        q = deque()
        close , open = 0 , 0
        ans = []
        for c in s:
            if c == "(":
                open += 1
            else:
                close += 1
            if close == open:
                q.popleft()
                ans.append("".join(q))
                q = deque()
            else:
                q.append(c)
        print(ans)
        return "".join(ans)