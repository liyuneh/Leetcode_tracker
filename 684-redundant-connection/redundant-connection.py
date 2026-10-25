class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return parent[x]
        def union(x, y):
            a, b = find(x), find(y)
            if a == b:
                return 
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True
        
        ans = []
        for i, j in edges:
            a , b = find(i), find(j)
            if a == b:
                if ans:
                    ans.pop()
                ans.append([i, j])
            else:
                union(i, j)
        a = ans.pop()
        return a
