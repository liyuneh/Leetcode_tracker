class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ["a","b","c"]
        res = []
        path = []
        def backtrack():
            if len(path) == n:
                res.append("".join(path))
                print(path)
                return 
            for i in range(len(s)):
                if path and path[-1] == s[i]:
                    continue
                path.append(s[i])
                backtrack()
                path.pop()
        backtrack()
        return res[k-1] if len(res) >= k else ""