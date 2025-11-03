class Solution:
    def minCost(self, colors: str, needTime: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                ans += min(needTime[l], needTime[r])
                if needTime[l] < needTime[r]:
                    l = r
            else:
                l = r
        return ans
