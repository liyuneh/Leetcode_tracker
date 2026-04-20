class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white, gray , black = 1, 2, 3
        color = {k:white for k in range(numCourses)}
        no_cycle = True
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            if color[node] == gray:
                return False
            if color[node] == black:
                return True
            color[node] = gray
            for ch in graph[node]:
                if not dfs(ch):
                    return False
            color[node] = black
            return True
        for i in range((numCourses)):
            if color [i] == white:
                if not dfs(i):
                    return False
                
        return True