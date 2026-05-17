class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def inbound(i): return 0 <= i < n
        value = set()
        for i in range(n):
            if arr[i] == 0:
                value.add(i)
        visited = set()
        def dfs(i):
            if not inbound(i) or i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])
        
        return dfs(start)