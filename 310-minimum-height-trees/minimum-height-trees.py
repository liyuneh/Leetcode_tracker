class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = [[] for _ in range(n )]
        indeg = [0] * (n)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        dist = [0] * (n)
        q = deque()
        for c in range(n):
            if indeg[c] == 1:
                q.append(c)
        rem = n
        while rem > 2 :
            rem -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for ne in graph[node]:
                    indeg[ne] -= 1
                    if indeg[ne] == 1:
                        q.append(ne)
        
        return list(q)