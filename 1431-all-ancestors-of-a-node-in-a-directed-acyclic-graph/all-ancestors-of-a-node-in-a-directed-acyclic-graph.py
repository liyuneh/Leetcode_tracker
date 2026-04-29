class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        ans = [set() for _ in range(n)]
        for c, pre in edges:
            graph[c].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for c in range(n):
            if indegree[c] == 0:
                q.append(c)
        while q:
            node = q.popleft()
            for ch in graph[node]:
                ans[ch] |= ans[node]
                ans[ch].add(node)
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    q.append(ch)
        return [sorted(nums) for nums in ans]