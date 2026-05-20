class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])
        def inbound(i, j) : return 0 <= i < n and 0 <= j < m
        dxn = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(i, j, visited, prev ):
            if not  inbound(i , j) or (i, j) in visited or heights[i][j] < prev:
                return 
            visited.add((i, j))
            for dx , dy in dxn:
                dfs(i + dx, j + dy, visited, heights[i][j])
        pac, atl = set() , set()
        for i in range(m):
            dfs(0, i , pac, heights[0][i])
            dfs(n - 1, i, atl, heights[n - 1][i])
        for i in range(n):
            dfs(i, 0 , pac,heights[i][0])
            dfs(i, m - 1, atl,heights[i][m - 1])
        ans = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])
        print(ans)
        return ans