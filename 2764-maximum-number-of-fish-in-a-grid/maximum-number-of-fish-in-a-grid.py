class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dxn = [(-1, 0), (0, -1), (1,0), (0,1)]
        n , m = len(grid), len(grid[0])
        def inbound(i, j): return 0<= i < n and 0 <= j < m
        def bfs(i, j , visited):
            q = deque([(i, j)])
            visited.add((i, j))
            ans = 0
            while q:
                x, y = q.popleft()
                ans += grid[x][y]
                for dx, dy in dxn:
                    nr, nc = dx + x, dy + y
                    if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != 0:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return ans
        mx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    mx = max(mx, bfs(i, j, set()))
        return mx