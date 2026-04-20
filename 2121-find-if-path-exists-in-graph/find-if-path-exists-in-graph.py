class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for v, u in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, visited):
            if destination  == node:
                return True
            visited.add(node)
            for ch in graph[node]:
                if ch not in visited:
                    found = dfs(ch, visited)
                    if found:
                        return True
            return False
        visited = set()
        return dfs(source, visited)