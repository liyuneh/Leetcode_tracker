class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = None
        path = []
        used = [False] * 10

        def backtrack():
            nonlocal res
            if res is not None:
                return
            if len(path) == len(pattern) + 1:
                res = "".join(path)
                return
            for i in range(1, 10):
                if used[i]:
                    continue
                if path:
                    prev = int(path[-1])
                    if pattern[len(path) - 1] == 'I' and prev > i:
                        continue
                    if pattern[len(path) - 1] == 'D' and prev < i:
                        continue
                used[i] = True
                path.append(str(i))
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res