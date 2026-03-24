class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid[0])
        pref = [[0] * m for _ in range(len(grid)) ]
        # print(pref)
        suff = [[0] * m for _ in range(len(grid))]
        prefs, suffs = 1, 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pref[i][j] = prefs
                prefs = (prefs  * grid[i][j]) % 12345
        # print(pref)
        
        for i in range(len(grid) - 1, -1 , -1):
            for j in range(m - 1, -1, -1):
                suff[i][j] = suffs
                suffs = (suffs * grid[i][j]) % 12345
        
        ans = [[0] * m for _ in range(len(grid))]
        for i in range(len(pref)):
            for j in range(len(pref[0])):
                ans[i][j] = (pref[i][j] * suff[i][j]) % 12345
        print(ans)
        
        return ans