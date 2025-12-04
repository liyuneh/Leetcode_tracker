class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        ans = 0
        for c in directions:
            if c == 'R':
                stack.append('R')
            elif c == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    ans += 1
                stack.append('S')
            else:
                if stack and stack[-1] == 'R':
                    ans += 2
                    stack.pop()
                    while stack and stack[-1] == 'R':
                        stack.pop()
                        ans += 1
                    stack.append('S')
                elif stack and stack[-1] == 'S':
                    ans += 1
                else:
                    stack.append('L')
        return ans
