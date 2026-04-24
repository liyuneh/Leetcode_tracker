class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node, path):
            if node == n - 1:
                ans.append(path[:])
                return 
            for y in graph[node]:
                path.append(y)
                dfs(y, path)
                path.pop()
        dfs(0, [0])
        print(ans)
        return ans