class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]
        degree = [0] * (n)
        for u in range(len(edges)):
            if edges[u] != -1:
                graph[u].append(edges[u])
                degree[edges[u]] += 1
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1

            for ne in graph[node]:
                degree[ne] -= 1
                if degree[ne] == 0:
                    q.append(ne)
        if count == n:
            return -1
        visited = set()

        def dfs(node):
            cnt = 0

            while node not in visited:
                visited.add(node)
                cnt += 1
                node = graph[node][0]

            return cnt
        ans = -1
        for i in range(n):
            if degree[i] > 0 and i not in visited:
                ans = max(ans, dfs(i))
        # print(ans)
        return ans