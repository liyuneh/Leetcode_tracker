class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mx = 0
        for u, v in edges:
            mx = max(mx, u,v)
        graph = [[] for _ in range(mx + 1)]
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque([1])
        depth = [-1] * (mx + 1)
        depth[1] = 0

        ans = 0
        while q:
            node = q.popleft()
            for ne in graph[node]:
                if depth[ne] == -1:
                    depth[ne] = depth[node] + 1
                    q.append(ne)
                    ans = max(ans, depth[ne])
    
        return pow(2, ans - 1, 10 ** 9 + 7)