class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        dp = [[0] * 26 for _ in range(n)]
        
        count = 0
        answer = 0

        while q:
            node = q.popleft()
            count += 1
            c = ord(colors[node]) - ord('a')
            dp[node][c] += 1
            answer = max(answer, dp[node][c])


            for ne in graph[node]:
                for k in range(26):
                    dp[ne][k] = max(dp[ne][k], dp[node][k])

                degree[ne] -= 1
                if degree[ne] == 0:
                    q.append(ne)
        if count != n:
            return -1
        
        
        return answer