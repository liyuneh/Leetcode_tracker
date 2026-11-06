class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        lg = collections.deque(sorted(logs,key = lambda x :x[1]))
        lgo = collections.deque()
        queries = sorted(enumerate(queries), key = lambda a:a[1])

        live = collections.Counter()
        ans = [0] * len(queries)

        for ind, q in queries:

            while len(lg) > 0 and lg[0][1] <= q:
                sid, t = lg.popleft()
                live[sid] += 1
                lgo.append((sid, t + x))
            while len(lgo) > 0 and lgo[0][1] < q:
                sid, t = lgo.popleft()
                live[sid] -= 1
                if live[sid] == 0:
                    del live[sid]
            ans[ind] = n -  len(live)
        return ans