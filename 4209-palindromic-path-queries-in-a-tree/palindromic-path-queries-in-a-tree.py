class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def update(self, i: int, val: int) -> None:
        while i <= self.n:
            self.tree[i] ^= val
            i += self.lowbit(i)

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res ^= self.tree[i]
            i -= self.lowbit(i)
        return res

    def update_range(self, left: int, right: int, val: int) -> None:
        self.update(left, val)
        self.update(right + 1, val)


class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        log = n.bit_length()
        parent = [[0] * log for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u: int, p: int) -> None:
            nonlocal timer
            timer += 1
            tin[u] = timer
            parent[u][0] = p

            for v in graph[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)

            tout[u] = timer

        dfs(0, 0)

        for j in range(1, log):
            for u in range(n):
                parent[u][j] = parent[parent[u][j - 1]][j - 1]

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(log):
                if (diff >> j) & 1:
                    u = parent[u][j]

            if u == v:
                return u

            for j in range(log - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            return parent[u][0]

        def char_mask(c: str) -> int:
            return 1 << (ord(c) - ord('a'))

        bit = BIT(n + 1)
        chars = list(s)

        for u in range(n):
            bit.update_range(tin[u], tout[u], char_mask(chars[u]))

        ans = []

        for query in queries:
            op, *args = query.split()

            if op == "update":
                u = int(args[0])
                c = args[1]

                change = char_mask(chars[u]) ^ char_mask(c)
                bit.update_range(tin[u], tout[u], change)
                chars[u] = c

            else:
                u, v = map(int, args[:2])
                w = lca(u, v)

                mask = (
                    bit.query(tin[u])
                    ^ bit.query(tin[v])
                    ^ char_mask(chars[w])
                )

                ans.append(mask.bit_count() <= 1)

        return ans
