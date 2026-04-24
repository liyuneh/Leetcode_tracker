class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        for i in range(n):
            x,y, r = bombs[i]
            for j in range(n):
                x2,y2, r2 = bombs[j]
                if i == j:
                    continue
                z = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
                if r >= z:
                    graph[i].append(j)
        def dfs(node, visited):
            visited.add(node)
            ans = 1
            for a in graph[node]:
                if a not in visited:
                    ans += dfs(a, visited)
            return ans 
        final = 0
        for i in range(n):
            visited = set()
            final = max(final, dfs(i, visited))
        # print(final)
        return final