class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        l , r = 0 , 1
        mx = intervals[l][1]
        while r < len(intervals):
            if mx >= intervals[r][0]:
                mx = max(mx, intervals[r][1])
            else:
                res.append([intervals[l][0], mx])
                mx = intervals[r][1]
                l = r
            
            r += 1
        if l < len(intervals):
            res.append([intervals[l][0], max(intervals[-1][1], mx)])
        return res