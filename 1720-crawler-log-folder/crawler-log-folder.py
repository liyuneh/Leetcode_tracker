class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for c in logs:
            if stack and c == "../":
                stack.pop()
            elif c == "./":
                continue
            elif c != "../":
                stack.append(c)
        return len(stack)