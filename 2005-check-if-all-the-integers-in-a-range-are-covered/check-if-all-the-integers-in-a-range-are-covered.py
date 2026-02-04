class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x:x[0])
        res = []
        l , r = 0 , 1
        mx = ranges[l][1]
        while r < len(ranges):
            if mx >= ranges[r][0]:
                mx = max(mx, ranges[r][1])
            else:
                res.append([ranges[l][0], mx])
                mx = ranges[r][1]
                l = r
            
            r += 1
        if l < len(ranges):
            res.append([ranges[l][0], max(ranges[-1][1], mx)])
        f1 = float('inf')
        for i in range(len(res)):
            if res[i][0] <= left and left <= res[i][1]:
                f1 = i
                break
        if f1 == float('inf'):
            return False
        f2 = float('inf')
        for i in range(len(res)):
            if res[i][1] >= right and right >= res[i][0]:
                f2 = i
                break
        if f2 == float('inf'):
            return False
        
        for i in range(f1, f2 ):
            if res[i+1][0] - res[i][1] > 1:
                return False
        return True

        
        