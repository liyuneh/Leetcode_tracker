class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        stack = []
        for first , second in intervals:
            if not stack:
                stack.append([first,second])
            elif stack and stack[-1][1] >= first:
                new_fir, new_sec = stack.pop()
                stack.append([new_fir,max(second, new_sec)])
            elif stack and stack[-1][1] < first:
                stack.append([first,second])
        # print(stack)
        return stack