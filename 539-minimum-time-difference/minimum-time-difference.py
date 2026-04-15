class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = []
        for i in range(len(timePoints) - 1):
            h, m = timePoints[i].split(":")
            h1, m1 = timePoints[i + 1].split(":")
            h = int(h) * 60 + int(m)
            h1 = int(h1) * 60 + int(m1)
            if h1 - h > 720:
                ans.append(1440 - (h1 - h))
            else:
                ans.append(h1 - h)
        h, m = timePoints[0].split(":")
        h1, m1 = timePoints[-1].split(":")
        h = int(h) * 60  + int(m)
        h1 = int(h1) * 60 + int(m1)
        if h1 - h > 720:
            ans.append(1440 - (h1 - h))
        else:
            ans.append(h1 - h)
        mn = float("inf")
        # print(timePoints)
        # print(ans)
        for i in range(len(ans)):
            mn = min(mn, ans[i])
        
        # print(mn)

        return mn