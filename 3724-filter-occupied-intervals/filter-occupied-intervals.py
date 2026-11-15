class Solution:
    def filterOccupiedIntervals(self, intervals: List[List[int]], freeS: int, freeE: int) -> List[List[int]]:
        stack = []
        # intervals.append([freeStart, freeEnd])
        intervals.sort(key = lambda x:(x[0], x[1]))

        for start, end in intervals:
            if not stack :
                stack.append([start, end])
            elif stack and stack[-1][1] < start:
                stack.append([start, end])
            elif stack and stack[-1][1] >= start:
                a , b = stack.pop()
                mn , mx = min(a, start), max(b, end)
                stack.append([mn,mx])
        # print(stack)
        # print()
        leftside = rightside =  0
        now = []
        for start, end in stack:
            if (end < freeS) or (start > freeE):
                now.append([start,end])
            elif start < freeS and end >= freeS:
                now.append([start, freeS - 1])
                if end > freeE:
                    now.append([freeE + 1, end])
            elif start <= freeE and end > freeE:
                now.append([freeE + 1,end])
        print(now)
        print()
        st = []
        for start , end in now:
            if not st:
                st.append([start,end])
            elif st and start - st[-1][1] <= 1:
                a, b = st.pop()
                st.append([a,end])
            else:
                st.append([start,end])

        # print(st)
        return st