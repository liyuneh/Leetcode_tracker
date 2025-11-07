class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count = 0
        cur = float('-inf')
        for start , end in points:
            if start > cur :
                count += 1
                cur  = end
        return count