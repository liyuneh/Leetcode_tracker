class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans.append(grid[i][j])
        ans.sort()
        s = []
        for i in range(len(ans)):
            b = ans[i] % x
            s.append(b)
        if len(set(s)) != 1:
            return -1
        z = len(ans) // 2 
        print(ans[z], ans[z -1])
        count = 0
        pref = 0
        for i in range(len(ans)):
            count += (abs(ans[i] - ans[z]) // x)
            pref += (abs(ans[i] - ans[z-1]) // x)
        return min(count, pref)