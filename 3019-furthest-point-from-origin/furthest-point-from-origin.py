class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        if "L" not in moves and "R" not in moves:
            return len(moves)
        ans = 0
        def dfs(i, pos):
            nonlocal ans
            if i == len(moves):
                ans = max(ans, abs(pos))
                return 
            if moves[i] == "L":
                dfs(i + 1, pos -1)
            elif moves[i] == "R":
                dfs(i + 1, pos + 1)
            else:
                dfs(i + 1, pos -1)
                dfs(i + 1, pos + 1)
        dfs(0, 0)
        return ans