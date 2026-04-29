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
        for c in range(1, n + 1):
            if indegree[c] == 0:
                q.append(c)
        count = 0
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                ans[node] += time[node - 1]
                for ch in graph[node]:
                    ans[ch] = max(ans[ch], ans[node])
                    indegree[ch] -= 1
                    if indegree[ch] == 0:
                        q.append(ch)
        return max(ans)  