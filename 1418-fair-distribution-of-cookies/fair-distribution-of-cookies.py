class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minimum = float("inf")
        path = [0] * k
        def backtrack(i, path):
            nonlocal minimum
            if i >= len(cookies):
                minimum = min(minimum, max(path))
                return 
            for j in range(k):
                path[j] += cookies[i]
                backtrack(i + 1, path)
                path[j] -= cookies[i]
        backtrack(0, path)
        return minimum