class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        
        forbidden = set(forbidden)
        q = deque([(0, False)])
        visited = {(0, False)}

        count = 0
        l = max(max(forbidden, default = 0), x) + a + b

        while q:
            for _ in range(len(q)):
                pos, prev = q.popleft()
                if pos == x:
                    return count
                
                forward = pos + a

                if forward <= l and forward not in forbidden:
                    state = (forward, False)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)
                backward = pos - b
                if not prev and backward >= 0 and backward not in forbidden:
                    state = (backward, True)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)
            count += 1
        return - 1