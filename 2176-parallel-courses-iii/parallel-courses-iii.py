class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if not relations:
            return max(time)
        indegree = [0 for _ in range(n + 1)]
        graph = [[] for _ in range(n + 1)]
        ans = [0] * (n + 1)
        for c, pre in relations:
            graph[c].append(pre)
            indegree[pre] += 1
        q = deque()
        dist = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                dist[node] += time[node - 1]
                for ne in graph[node]:
                    indegree [ne] -= 1
                    dist[ne] = max(dist[ne], dist[node])
                    if indegree[ne] == 0:
                        q.append(ne) 
        print(max(dist))
        return max(dist)