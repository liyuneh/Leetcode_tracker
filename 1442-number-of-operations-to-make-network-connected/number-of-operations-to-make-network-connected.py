class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return parent[x]
        def union(x, y):
            a, b = find(x), find(y)
            if a == b:
                return False
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True
        
        
        cnt = n
        for i,j in connections:
            if union(i, j):
                cnt -= 1
        return cnt - 1