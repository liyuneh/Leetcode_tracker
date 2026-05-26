class Solution:
    def numSquares(self, n: int) -> int:

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        q = deque([n])
        level = 0
        visited = set([n])
        while q:
            level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for sq in squares:
                    nxt = cur - sq
                    if nxt < 0:
                        continue
                    if nxt == 0:
                        return level
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)