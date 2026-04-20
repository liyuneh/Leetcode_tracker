class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        def dfs(node, graph):
            temp = True
            for ch in graph[node]:
                if color[ch] == -1:
                    if color[node] == 0:
                        color[ch] = 1
                    else:
                        color[ch] = 0
                    temp = temp and dfs(ch, graph)
                elif color[ch] == color[node]:
                    return False
            return temp
        result = True
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                result  = result and dfs(i, graph)
        return result