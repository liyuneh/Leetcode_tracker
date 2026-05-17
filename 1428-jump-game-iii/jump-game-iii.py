class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def inbound(i): return 0 <= i < n
        q = deque([start])
        visited = set([start])

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            one , two = i - arr[i], i + arr[i]
            if inbound(one) and one not in visited:
                visited.add(one)
                q.append(one)
            if inbound(two) and two not in visited:
                visited.add(two)
                q.append(two)
        return False