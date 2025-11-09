class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        stack = []
        for c in intervals:
            if not stack:
                stack.append(c)
            elif stack and stack[-1][1] >= c[0]:
                x = stack.pop()
                x1 = min(x[0], c[0])
                y = max(x[1], c[1])
                stack.append([x1,y])
            else:
                stack.append(c)
        return stack