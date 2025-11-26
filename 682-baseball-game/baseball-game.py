class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if stack and c == "C":
                stack.pop()
            elif stack and c == "D":
                stack.append(stack[-1] * 2)
            elif len(stack) > 1 and c == "+":
                k = stack[-1] + stack[-2]
                stack.append(k)
            else:
                stack.append(int(c))
        print(stack)
        return sum(stack)