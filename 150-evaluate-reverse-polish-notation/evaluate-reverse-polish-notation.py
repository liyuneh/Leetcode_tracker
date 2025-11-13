class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ('-+*/') :
                stack.append(int(c))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if c == '*':
                    stack.append(val1 * val2)
                elif c == '+':
                    stack.append(val1 + val2)
                elif c == '/':
                    stack.append(int(val2 /val1))
                else:
                    stack.append(val2 - val1)
        return stack[0]